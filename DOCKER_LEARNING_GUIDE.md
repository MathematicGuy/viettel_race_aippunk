# Docker & Milvus: From Basics to Production

## Table of Contents
1. [Docker Fundamentals](#docker-fundamentals)
2. [Docker vs Traditional Setup](#docker-vs-traditional-setup)
3. [Docker + Milvus: What's New](#docker--milvus-whats-new)
4. [Understanding Your docker-compose.yml](#understanding-your-docker-composeyml)
5. [How It All Works Together](#how-it-all-works-together)

---

## Docker Fundamentals

### What is Docker?

Docker is a **containerization platform** that packages your application and all its dependencies (libraries, runtime, code) into a single, isolated unit called a **container**.

Think of it like shipping containers:
- 📦 **Traditional Way**: You send individual items (Python, PostgreSQL, Node.js, etc.) separately, and they might not work together
- 🚢 **Docker Way**: You pack everything into one sealed container that works exactly the same everywhere

### Core Concepts

#### 1. **Image**
A **blueprint** or **template** for creating containers.
```
IMAGE = Recipe
CONTAINER = Cooked dish
```

**Example**:
```dockerfile
# Dockerfile - defines an image
FROM python:3.11
RUN pip install flask
COPY app.py /app/
ENTRYPOINT ["python", "app.py"]
```

When you build this → **Image created**

When you run this image → **Container starts**

#### 2. **Container**
A **running instance** of an image. It's isolated and has:
- Own filesystem
- Own network interface
- Own processes
- Own memory

```bash
docker run python:3.11  # Start 1 container from python image
docker run python:3.11  # Start another container (independent)
```

#### 3. **Docker Hub**
A **registry** (like GitHub but for Docker images). Pre-made images you can use:
```bash
docker pull milvusdb/milvus:v2.6.3  # Download Milvus image
docker pull postgres:15              # Download PostgreSQL image
```

#### 4. **Volume**
A **persistent storage** mechanism. Containers are temporary, but volumes survive:

```
Container (temporary, created/destroyed)
    ↓
Volume (permanent, persists)
    ↓
Your hard drive
```

**Example**:
```yaml
volumes:
  - ./data:/app/data  # Maps local ./data → container /app/data
```

#### 5. **Network**
Allows containers to **communicate** with each other:

```
Container A ←→ Network ←→ Container B
```

---

## Docker vs Traditional Setup

### Scenario: Running a Database Application

#### ❌ Traditional Way (No Docker)
```
1. Download PostgreSQL installer
2. Download Node.js installer
3. Download Python installer
4. Install each manually
5. Configure PATH variables
6. Start each service manually
7. Hope everything works...

Colleagues: "Works on my machine!" 😅
Production: Crashes because versions differ
```

**Problems**:
- ⚠️ Installation is complex and error-prone
- ⚠️ Works on one machine, breaks on another
- ⚠️ Hard to scale (running 10 instances = 10x setup work)
- ⚠️ Conflicts with existing software

#### ✅ Docker Way
```
1. Write Dockerfile (describes setup once)
2. Build image
3. Run container anywhere (laptop, server, cloud)

Same setup everywhere! 🎯
```

**Benefits**:
- ✅ Consistency across all machines
- ✅ Easy scaling (run 100 containers instantly)
- ✅ No conflicts (isolated from host system)
- ✅ Quick deployment

---

## Docker + Milvus: What's New

### Understanding Milvus First

**Milvus** is a vector database for AI/ML applications. It's complex with multiple components:

```
Milvus System (Traditional Installation)
├── etcd              (metadata management)
├── MinIO             (object storage)
├── Milvus Server     (query engine)
├── Proxy             (client interface)
└── Message Queue     (communication)

Installation steps: 30+ pages in docs 😰
```

### Docker + Milvus: Simplified!

Instead of installing 5+ services manually, your `docker-compose.yml` does this:

```yaml
services:
  etcd:         # One service = one container
  minio:        # One service = one container
  standalone:   # One service = one container
  attu:         # One service = one container

docker-compose up -d  # Start all 4 containers in one command! 🚀
```

### What's New with Docker + Milvus

| Aspect | Without Docker | With Docker |
|--------|---|---|
| **Setup Time** | 2-3 hours | 5 minutes |
| **Components** | Install 5+ services manually | Pre-built images, just configure |
| **Networking** | Configure each port/firewall | Automatic internal network |
| **Data Persistence** | Manual backup strategy | Volumes (automatic persistence) |
| **Team Consistency** | "Works on my machine" | Works everywhere |
| **Scaling** | Redo all steps N times | `docker-compose scale` |
| **Cleanup** | Manual uninstall | `docker-compose down` |

---

## Understanding Your docker-compose.yml

### What is docker-compose?

`docker-compose` is a tool that lets you define and run **multiple containers** at once using a YAML file.

```
Instead of: docker run ... (manual for each container)
You write:  docker-compose.yml (describes all containers)
Then run:   docker-compose up -d (start everything)
```

### Your Setup: 4 Containers Working Together

```
┌─────────────────────────────────────────────────────┐
│  Your Application (Python code)                     │
└──────────────────┬──────────────────────────────────┘
                   │ (connects to port 19530)
                   ▼
┌─────────────────────────────────────────────────────┐
│  Docker Network: "milvus"                           │
│  ┌──────────────┬──────────────┬──────────────┐    │
│  │              │              │              │    │
│  ▼              ▼              ▼              ▼    │
│ etcd          minio         standalone       attu  │
│ :2379         :9000/:9001    :19530/:9091   :3000 │
│ (metadata)    (storage)      (main server)  (UI)  │
│              │              │              │    │
│  └──────────────┴──────────────┴──────────────┘    │
└─────────────────────────────────────────────────────┘
         ▲            ▲            ▲
         │            │            │
      volumes: etcd  volumes:minio volumes:milvus
      (persists)     (persists)    (persists)
```

---

## Each Component Explained

### 1️⃣ **etcd - Metadata Storage** 🗄️

```yaml
services:
  etcd:
    container_name: milvus-etcd
    image: quay.io/coreos/etcd:v3.5.18
    environment:
      - ETCD_AUTO_COMPACTION_MODE=revision
      - ETCD_AUTO_COMPACTION_RETENTION=1000
      - ETCD_QUOTA_BACKEND_BYTES=4294967296
      - ETCD_SNAPSHOT_COUNT=50000
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/etcd:/etcd
    command: etcd -advertise-client-urls=http://etcd:2379 -listen-client-urls http://0.0.0.0:2379 --data-dir /etcd
    healthcheck:
      test: ["CMD", "etcdctl", "endpoint", "health"]
      interval: 30s
      timeout: 20s
      retries: 3
```

#### What is etcd?

**etcd** = "etc distributed" - a distributed key-value store that stores **metadata**.

#### What metadata is stored here?

```
✓ Database names
✓ Collection schemas (structure)
✓ Field definitions
✓ Index information
✓ Partition information
✓ System configuration

Example:
database: "gil"
collection: "multimodal_rag"
fields: [id, embedding, text, metadata]
```

#### Key Settings Explained

| Setting | Meaning |
|---------|---------|
| `ETCD_AUTO_COMPACTION_MODE=revision` | Automatically clean old data |
| `ETCD_AUTO_COMPACTION_RETENTION=1000` | Keep last 1000 revisions |
| `ETCD_QUOTA_BACKEND_BYTES=4294967296` | Max 4GB storage |
| `ETCD_SNAPSHOT_COUNT=50000` | Save state every 50k changes |

#### Volume Mapping

```yaml
volumes:
  - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/etcd:/etcd
```

This means:
- **Local path**: `./volumes/etcd` (on your computer)
- **Container path**: `/etcd` (inside etcd container)
- **Effect**: Whatever etcd writes to `/etcd` appears in `./volumes/etcd` on your computer

If you delete the container, data persists! ✅

#### Health Check

```yaml
healthcheck:
  test: ["CMD", "etcdctl", "endpoint", "health"]
  interval: 30s
  timeout: 20s
  retries: 3
```

Docker checks every 30 seconds if etcd is healthy. If it fails 3 times, Docker can restart it automatically.

---

### 2️⃣ **MinIO - Object Storage** 💾

```yaml
services:
  minio:
    container_name: milvus-minio
    image: minio/minio:RELEASE.2024-12-18T13-15-44Z
    environment:
      MINIO_ACCESS_KEY: minioadmin
      MINIO_SECRET_KEY: minioadmin
    ports:
      - "9001:9001"
      - "9000:9000"
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/minio:/minio_data
    command: minio server /minio_data --console-address ":9001"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9000/minio/health/live"]
      interval: 30s
      timeout: 20s
      retries: 3
```

#### What is MinIO?

**MinIO** = S3-compatible object storage (like AWS S3 but self-hosted).

It stores **large binary data**:
```
✓ Vector embeddings (dense vectors)
✓ BM25 indices (sparse vectors)
✓ Index files
✓ Segment data
```

#### Ports Explained

```yaml
ports:
  - "9001:9001"  # Console UI (web browser interface)
  - "9000:9000"  # API port (for programmatic access)
```

**Port Mapping**: `<host_port>:<container_port>`

```
Your Computer          Container
port 9001      ←→      port 9001 (MinIO UI)
port 9000      ←→      port 9000 (MinIO API)

Open browser: http://localhost:9001
Login: minioadmin / minioadmin
```

#### Environment Variables

```yaml
MINIO_ACCESS_KEY: minioadmin    # Username
MINIO_SECRET_KEY: minioadmin    # Password

⚠️ NOTE: Change these in production!
```

#### Volume Mapping

```yaml
volumes:
  - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/minio:/minio_data
```

```
./volumes/minio/    ←→    /minio_data (inside container)
(Your computer)            (Container storage)
```

All vector data is saved here! 📊

---

### 3️⃣ **standalone - Milvus Server** 🧠

```yaml
services:
  standalone:
    container_name: milvus-standalone
    image: milvusdb/milvus:v2.6.3
    command: ["milvus", "run", "standalone"]
    security_opt:
      - seccomp:unconfined
    environment:
      ETCD_ENDPOINTS: etcd:2379
      MINIO_ADDRESS: minio:9000
      MQ_TYPE: woodpecker
    volumes:
      - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/milvus:/var/lib/milvus
    ports:
      - "19530:19530"
      - "9091:9091"
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:9091/healthy"]
      interval: 30s
      start_period: 90s
      timeout: 20s
      retries: 3
    depends_on:
      - "etcd"
      - "minio"
```

#### What is Milvus Standalone?

**Milvus Standalone** = The main vector database server that:
- Creates/manages collections
- Handles vector searches
- Processes queries
- Manages indices

#### Environment Variables

```yaml
ETCD_ENDPOINTS: etcd:2379
```

"Tell Milvus where to find etcd"

```
Milvus (standalone:19530)
    ↓ (knows where to find metadata)
etcd:2379 (inside docker network)
```

```yaml
MINIO_ADDRESS: minio:9000
```

"Tell Milvus where to find MinIO"

```
Milvus (standalone:19530)
    ↓ (knows where to find storage)
minio:9000 (inside docker network)
```

```yaml
MQ_TYPE: woodpecker
```

"Use Woodpecker as message queue"

(Message queue = communication between Milvus components)

#### Ports

```yaml
ports:
  - "19530:19530"  # ← Your Python code connects here!
  - "9091:9091"    # ← Health check endpoint
```

```python
# In your milvus_store.py:
self.uri = "http://localhost:19530"  # ← This port!
```

#### Dependencies

```yaml
depends_on:
  - "etcd"
  - "minio"
```

"Start Milvus only after etcd and MinIO are ready"

#### Volume

```yaml
volumes:
  - ${DOCKER_VOLUME_DIRECTORY:-.}/volumes/milvus:/var/lib/milvus
```

Milvus internal data stored here (indices, metadata cache, etc.)

#### Health Check - Important!

```yaml
healthcheck:
  test: ["CMD", "curl", "-f", "http://localhost:9091/healthy"]
  interval: 30s
  start_period: 90s    # ← Give Milvus 90s to start
  timeout: 20s
  retries: 3
```

⚠️ **start_period: 90s** = Give Milvus 90 seconds to initialize before checking health

This is important because Milvus needs time to connect to etcd and MinIO!

---

### 4️⃣ **attu - Management UI** 🎨

```yaml
services:
  attu:
    container_name: milvus-attu
    image: zilliz/attu:latest
    environment:
      - MILVUS_URL=milvus-standalone:19530
    ports:
      - "8000:3000"
    depends_on:
      - standalone
    networks:
      - default
```

#### What is Attu?

**Attu** = Web UI for managing Milvus collections (like phpMyAdmin for MySQL).

#### Environment Variable

```yaml
MILVUS_URL=milvus-standalone:19530
```

"Tell Attu where Milvus server is"

Inside the Docker network, Attu knows the hostname `milvus-standalone` and connects to it.

#### Port

```yaml
ports:
  - "8000:3000"
```

```
Your Computer          Container
port 8000      ←→      port 3000 (Attu)

Open browser: http://localhost:8000
```

#### Use Case

After data is indexed, visit `http://localhost:8000` to:
- ✅ View databases
- ✅ View collections
- ✅ View documents count
- ✅ Test queries
- ✅ Manage metadata

---

### 5️⃣ **Network Configuration**

```yaml
networks:
  default:
    name: milvus
```

#### What is the Network?

Creates a Docker network named `milvus` so all containers can talk to each other:

```
etcd ←→ (docker network: milvus) ←→ minio
  ↑                                    ↑
  └────────← standalone →─────────────┘
       ↑
       └─ attu
```

#### Container Hostnames

Inside the network:
- `etcd` → accessible as `etcd:2379`
- `minio` → accessible as `minio:9000`
- `standalone` → accessible as `standalone:19530` (or `milvus-standalone:19530`)

This is like internal DNS! 🌐

---

## How It All Works Together

### Step-by-Step Flow

#### 1. **Start Everything**
```bash
docker-compose up -d
```

```
↓ Docker reads docker-compose.yml
↓ Creates network "milvus"
↓ Starts etcd container (waits for health check)
↓ Starts MinIO container (waits for health check)
↓ Starts Milvus standalone (depends_on etcd & minio)
  └─ Milvus connects to etcd:2379
  └─ Milvus connects to minio:9000
↓ Starts Attu container (depends_on standalone)
✓ All ready!
```

#### 2. **Your Python Code Runs**

```python
from src.milvus_store import MilvusStore

store = MilvusStore(uri="http://localhost:19530")
```

```
Your code (localhost)
    ↓ (connects to port 19530)
Milvus standalone container
    ↓ (needs metadata)
etcd container
    ↓ (needs to store data)
MinIO container
    ↓ (saves to disk)
./volumes/minio/
```

#### 3. **Data Gets Stored**

```
store.add_documents(documents)
    ↓
Milvus creates indices
    ↓
Writes metadata to etcd → ./volumes/etcd/
    ↓
Writes vectors to MinIO → ./volumes/minio/
    ↓
Writes index data to Milvus → ./volumes/milvus/

✓ All persisted!
```

#### 4. **Container Restarts, Data Survives**

```bash
docker-compose down      # Stop all containers
docker-compose up -d     # Start again
```

```
✓ etcd reads from ./volumes/etcd/
✓ MinIO reads from ./volumes/minio/
✓ Milvus reads from ./volumes/milvus/

All your data is back! 🎯
```

#### 5. **View Data in UI**

```bash
# Open browser
http://localhost:8000  # Attu UI
```

```
You see:
- Database: "gil"
- Collection: "multimodal_rag"
- Document count: 1000+
- Partitions: by namespace
```

---

## Practical Commands

### Start Everything
```bash
docker-compose up -d
```
`-d` = detached mode (runs in background)

### View Logs
```bash
docker-compose logs -f milvus-standalone
```
`-f` = follow (shows new logs in real-time)

### Stop All
```bash
docker-compose down
```
Stops containers but **keeps data** (volumes persist)

### Complete Reset (Delete Data Too)
```bash
docker-compose down -v
```
`-v` = remove volumes (WARNING: deletes all data!)

### Check Status
```bash
docker-compose ps
```

Output:
```
NAME                 STATUS
milvus-etcd          Up 5 minutes (healthy)
milvus-minio         Up 5 minutes (healthy)
milvus-standalone    Up 4 minutes (healthy)
milvus-attu          Up 4 minutes
```

### View Specific Service Logs
```bash
docker-compose logs milvus-minio
docker-compose logs milvus-etcd
```

### Restart a Service
```bash
docker-compose restart milvus-standalone
```

---

## Troubleshooting

### Issue: "Connection refused on port 19530"

**Cause**: Milvus not ready yet

**Fix**: Wait 90+ seconds for health check to pass
```bash
docker-compose logs -f milvus-standalone
# Wait for: "healthy"
```

### Issue: "etcd volume permission denied"

**Cause**: Volume directory doesn't exist

**Fix**:
```bash
mkdir -p volumes/etcd volumes/minio volumes/milvus
docker-compose up -d
```

### Issue: "MinIO health check failed"

**Cause**: Port 9000 already in use

**Fix**: Change port in docker-compose.yml:
```yaml
ports:
  - "9002:9000"  # Use 9002 instead
  - "9001:9001"
```

---

## Summary: What You Now Understand

| Concept | Simple Explanation |
|---------|---|
| **Image** | Blueprint for container |
| **Container** | Running app instance |
| **Volume** | Persistent storage |
| **Port** | How to access container from outside |
| **Network** | How containers talk to each other |
| **etcd** | Metadata database for Milvus |
| **MinIO** | Vector storage (S3-compatible) |
| **Milvus Standalone** | Main vector database server |
| **Attu** | Web UI to manage Milvus |
| **docker-compose** | Define and run multiple containers at once |

---

## Next Steps

1. ✅ **Start containers**: `docker-compose up -d`
2. ✅ **Run your code**: `python main2.py`
3. ✅ **View results**: Open `http://localhost:8000` (Attu)
4. ✅ **Check data**: Run `docker-compose ps`
5. ✅ **Stop safely**: `docker-compose down`

**You now understand Docker and your Milvus setup!** 🚀

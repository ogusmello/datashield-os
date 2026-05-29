# DataShield OS

> Enterprise Data Governance & PII Classification Platform

![Python](https://img.shields.io/badge/Python-3.14-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Async-green)
![React](https://img.shields.io/badge/React-18-blue)
![TypeScript](https://img.shields.io/badge/TypeScript-Strict-informational)
![Redis](https://img.shields.io/badge/Redis-Workers-red)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)
![GCP](https://img.shields.io/badge/GCP-Cloud_Run-orange)

# Overview

**DataShield OS** is an enterprise-grade **Data Governance & Compliance Platform** designed to manage large-scale metadata ecosystems, classify Personally Identifiable Information (PII), and provide real-time auditability across distributed systems.

The platform was architected to simulate real-world enterprise governance challenges involving:

* GDPR & CCPA compliance
* hierarchical metadata management
* asynchronous ETL pipelines
* real-time collaborative auditing
* distributed lineage tracking
* large-scale frontend rendering
* event-driven infrastructure

DataShield OS enables security analysts and data engineers to operate as **Judges**, auditing data structures from high-level business applications down to individual database columns.

# Core Engineering Goals

## Replace Legacy Blocking Architectures

Migrate from traditional synchronous paradigms toward a fully asynchronous event-driven architecture powered by:

* FastAPI
* Redis Workers
* AsyncIO
* WebSockets

## Extreme Visual Scalability

Support smooth interaction with metadata catalogs containing **10,000+ live nodes** without client-side rendering bottlenecks.

## Enterprise-Level Architecture Demonstration

The project serves as a portfolio-grade proof of engineering maturity, emphasizing:

* scalable systems design
* asynchronous backend processing
* real-time communication
* strict typing discipline
* infrastructure readiness
* production-oriented architecture

# Tech Stack

## Frontend

* React 18
* Vite
* TypeScript (`strict: true`)
* React Window / Virtualization
* WebSockets
* Zustand or Redux Toolkit
* TailwindCSS

## Backend

* FastAPI
* Python 3.14
* SQLAlchemy 2.0
* Pydantic v2
* AsyncIO
* Redis
* Pytest

## Infrastructure

* Docker
* Docker Compose
* Redis Workers
* GCP Cloud Run
* Pipenv
* SQLite (local development)

# System Architecture

The platform models enterprise metadata as a strict hierarchical structure.

```text
Application
 ├── Schema
 │    ├── Table
 │    │    ├── Column
 │    │    └── Column
 │    └── Table
 └── Schema
```

This hierarchy represents real-world corporate data ownership and inheritance rules.

# Domain Model

## Applications

Root entities representing enterprise systems or services.

Examples:

* Checkout Service
* Sales CRM
* Customer Analytics Platform

Applications define:

* ownership
* global security scope
* metadata discovery context

## Connections

Mappings between enterprise applications and external infrastructure sources.

Examples:

* PostgreSQL
* MySQL
* BigQuery
* S3
* Snowflake

## Connectors
Supported infrastructure drivers responsible for ingestion and synchronization.

## Application Leafs
Represents the lowest-level auditable asset:

```text
database → table → column
```

Tracks:
* security levels
* PII classification
* audit status
* metadata inheritance
* confidence scoring
* structural mutations

## Application Leaf Reviews
Immutable audit history preserving every governance decision.

Supports:
* revision chaining
* historical rollback
* reviewer attribution
* compliance reproducibility

# Functional Requirements
## FR-01 — Hierarchical Catalog Navigation
Render an expandable enterprise metadata tree:

```text
Application → Schema → Table → Column
```

Features:
* lazy loading
* virtualization
* recursive rendering
* node expansion/collapse

## FR-02 — Judge Interface
Auditors can:
* classify security level
* override inherited metadata
* flag PII fields
* attach compliance justification

### Security Levels
* Low
* Medium
* High
* Critical

## FR-03 — Asynchronous ETL Discovery
The platform includes a metadata synchronization engine capable of:
* scanning external structures
* discovering new entities
* detecting schema mutations
* updating the catalog asynchronously

All heavy processing is delegated to Redis workers.

## FR-04 — Data Lineage Engine
Track metadata dependencies across systems.

Example:
```text
App A / users.email
        ↓
Consumed by
        ↓
App B / customer_notifications.recipient
```

If a source field becomes classified as PII:
* downstream systems receive impact alerts
* dependent classifications become review candidates

## FR-05 — Real-Time Synchronization
Every audit event must:
* persist immutably
* broadcast instantly
* synchronize across active sessions

Implemented via native FastAPI WebSockets.

# Non-Functional Requirements
## NFR-01 — Async-First Infrastructure
Critical endpoints must respond in:

```text
< 200ms
```

Heavy operations execute asynchronously:
* ETL jobs
* lineage calculations
* security propagation
* metadata reconciliation

## NFR-02 — Frontend Virtualization
The UI must maintain fluid rendering performance when handling:

```text
10,000+ simultaneously opened nodes
```

Techniques:
* DOM recycling
* windowed rendering
* tree virtualization

## NFR-03 — Extreme Type Safety
### Frontend

```json
{
  "strict": true
}
```

### Backend

* fully typed Pydantic models
* strict request validation
* typed SQLAlchemy mappings

Zero `any` policy.

## NFR-04 — Bidirectional Communication
WebSocket channels handle:

* ETL progress
* lineage propagation
* audit synchronization
* real-time notifications

## NFR-05 — Testing Standards
Minimum testing requirements:

```text
≥ 85% coverage
```

Validated through:
* pytest
* async integration testing
* lineage engine verification
* inheritance engine validation

# Backend Structure
```text
backend/
├── main.py
├── datashield_db.sqlite
├── modules/
│
├── core/
│   ├── database.py
│   └── models.py
│
├── users/
│   ├── controllers/
│   ├── helpers/
│   ├── models/
│   └── schemas/
│
└── application/
    ├── controllers/
    ├── models/
    └── schemas/
```

# Development Roadmap
# Phase 1 — Foundations (Months 1–2)

Focus:
* FastAPI architecture
* SQLAlchemy modeling
* strict TypeScript contracts
* CRUD foundations
* hierarchical metadata modeling

Deliverables:
* initial APIs
* relational schema
* frontend base layouts
* authentication scaffolding

# Phase 2 — Async Infrastructure (Months 3–4)
Focus:
* Redis workers
* ETL simulation pipelines
* background processing
* WebSocket event systems
* real-time synchronization

Deliverables:
* async metadata ingestion
* distributed processing
* live update infrastructure

# Phase 3 — Scale & Production Readiness (Months 5–6)
Focus:
* lineage engine
* cascading security propagation
* frontend virtualization
* Docker optimization
* Cloud Run deployment

Deliverables:
* production-ready infrastructure
* scalable rendering engine
* deployment orchestration

# Engineering Challenges
DataShield OS intentionally targets advanced engineering problems:
* distributed metadata consistency
* real-time synchronization
* lineage graph traversal
* cascading PII propagation
* event-driven processing
* async concurrency
* frontend rendering at scale
* immutable audit systems

# Nice-to-Have Features
## AI-Assisted Semantic Classification
LLM-powered workers capable of automatically inferring sensitive fields.

Example:
```text
usr_tel_num
```

Suggested classification:
```json
{
  "pii": true,
  "security_level": "HIGH"
}
```

## Native Dark Mode
Accessibility-oriented UI theme switching for long audit sessions.

# Local Development
## Backend

```bash
pipenv install
pipenv shell
uvicorn main:app --reload
```

## Frontend

```bash
npm install
npm run dev
```

## Redis
```bash
docker-compose up redis
```

# Docker
## Start Full Stack

```bash
docker-compose up --build
```

# Cloud Deployment
Target Infrastructure:

* Google Cloud Run
* Containerized workloads
* Stateless async services
* Redis-backed worker architecture

# Strategic Purpose
DataShield OS is intentionally designed as more than a CRUD application.

The platform demonstrates:
* enterprise-grade backend engineering
* scalable frontend architecture
* asynchronous distributed processing
* strict software quality standards
* production-oriented cloud infrastructure
* international-level engineering maturity
---

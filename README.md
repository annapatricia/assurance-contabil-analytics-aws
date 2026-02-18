# 📊 Accounting Assurance Analytics (AWS-Based Pipeline)

Cloud-ready analytics pipeline for accounting governance, compliance monitoring and anomaly detection.

This project simulates a structured assurance environment where accounting entries are generated, processed, uploaded to AWS S3, and analyzed for key performance indicators and anomalous transactions.

---

## 🎯 Objective

To demonstrate a governance-focused analytics workflow that:

- Generates structured accounting transaction data
- Uploads datasets to AWS S3
- Computes institutional accounting indicators
- Detects anomalies using machine learning
- Enables scalable cloud-based analytics architecture

---

## 🏗 Architecture Overview

The project is modularized under `src/`:

```
src/
│
├── config.py                # AWS configuration (region, bucket, prefix)
├── gerar_dados_contabeis.py # Synthetic accounting data generator
├── etl_s3.py                # S3 upload logic
├── indicadores.py           # KPI calculations
└── modelo_anomalias.py      # Anomaly detection model (Isolation Forest)
```

---

## 📂 Workflow

### 1️⃣ Generate Accounting Data

Synthetic accounting transactions are generated with:

- Accounting account
- Cost center
- User
- Debit/Credit type
- Manual vs Automatic classification
- Transaction value
- Timestamp

Run:

```bash
python src/gerar_dados_contabeis.py
```

Output:
```
lancamentos_contabeis.csv
```

---

### 2️⃣ Upload to AWS S3

The ETL layer uploads the dataset to a structured S3 prefix:

```bash
python src/etl_s3.py
```

Example S3 structure:

```
s3://seu-bucket-assurance-contabil/lancamentos_contabeis/ano=2024/mes=01/
```

---

### 3️⃣ Compute Accounting Indicators

KPIs include:

- Total transactions
- Percentage of manual entries
- Average transaction value

Implemented in:

```
src/indicadores.py
```

---

### 4️⃣ Anomaly Detection

Anomalies are detected using:

- Isolation Forest (Scikit-learn)
- Contamination rate: 1%

Implemented in:

```
src/modelo_anomalias.py
```

This enables identification of suspicious transaction patterns for audit and compliance purposes.

---

## ☁️ Cloud Configuration

Defined in:

```
src/config.py
```

Example:

```python
AWS_REGION = "us-east-1"
S3_BUCKET = "seu-bucket-assurance-contabil"
S3_PREFIX = "lancamentos_contabeis/"
```

Environment credentials should be configured via AWS CLI or IAM roles.

---

## 🛠 Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn (IsolationForest)
- AWS S3 (boto3)

---

## 🏢 Application Context

Designed for:

- Accounting assurance workflows
- Compliance monitoring systems
- Internal audit environments
- Governance, Risk & Compliance (GRC) analytics
- Cloud-based financial monitoring systems

---

## 🔮 Possible Extensions

- Integrate Athena for querying S3 data
- Connect to Power BI via S3/Athena
- Add time-series anomaly detection
- Add role-based transaction profiling
- Deploy as Lambda-based pipeline

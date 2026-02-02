import boto3
from config import AWS_REGION, S3_BUCKET, S3_PREFIX

s3 = boto3.client("s3", region_name=AWS_REGION)

def upload_arquivo(caminho_local, nome_arquivo):
    s3.upload_file(
        caminho_local,
        S3_BUCKET,
        f"{S3_PREFIX}{nome_arquivo}"
    )

if __name__ == "__main__":
    upload_arquivo(
        "lancamentos_contabeis.csv",
        "ano=2024/mes=01/lancamentos_contabeis.csv"
    )

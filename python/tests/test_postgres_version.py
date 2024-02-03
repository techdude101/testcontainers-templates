import os

from testcontainers.postgres import PostgresContainer

import sqlalchemy

def test_start_postgres_and_get_version():
  os.environ["DOCKER_HOST"] = "tcp://192.168.1.64:2375"
  
  with PostgresContainer("postgres:9.5") as postgres:

    engine = sqlalchemy.create_engine(postgres.get_connection_url())
    
    with engine.connect() as conn:
      result = conn.execute(sqlalchemy.text("SELECT VERSION()"))
      version, = result.fetchone()
      print(version)

  assert 'PostgreSQL 9.5' in version

def test_start_postgres_and_get_version_should_fail():
  os.environ["DOCKER_HOST"] = "tcp://192.168.1.64:2375"
  
  with PostgresContainer("postgres:9.5") as postgres:

    engine = sqlalchemy.create_engine(postgres.get_connection_url())
    
    with engine.connect() as conn:
      result = conn.execute(sqlalchemy.text("SELECT VERSION()"))
      version, = result.fetchone()
      print(version)

  assert version == 'PostgreSQL 9.5'
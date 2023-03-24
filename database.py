import os
from sqlalchemy import text, create_engine

DB_CONNECT_STRING = os.environ['DB_CONNECT_STRING']
engine = create_engine(my_secret,
                       connect_args={
                         "ssl":{
                            "ssl_ca":"/etc/ssl/cert.pem"
                         }
                       })

def load_job_from_db(): 
  with engine.connect() as conn:
      result = conn.execute(text("select * from jobs"))  
      jobs = []
      for row in result.all():
        jobs.append(row._asdict())
       
      return jobs
  

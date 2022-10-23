from ploomber import DAG
from ploomber.products import File
from ploomber.tasks import NotebookRunner
from ploomber.executors import Parallel

from pathlib import Path
from glob import iglob

dag = DAG(executor=Parallel())

# get all notebooks recursively in the current directory only
# (not in other upper directories)
notebooks = iglob("**/*.ipynb", recursive=True)


for path in notebooks:
    try:
        NotebookRunner(
            Path(path),
            File(path),
            dag=dag,
            papermill_params=dict(engine_name="embedded"),
        )
    except Exception as e:
        print(e)

if __name__ == "__main__":

    try:
        dag.build(force=True)
    except Exception as e:
        print(e)

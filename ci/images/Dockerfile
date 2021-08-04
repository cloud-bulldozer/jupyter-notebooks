FROM jupyter/minimal-notebook:lab-3.0.16

RUN jupyter serverextension enable --py jupyterlab --sys-prefix
RUN pip install nbgitpuller
RUN jupyter serverextension enable nbgitpuller --sys-prefix
RUN pip install --upgrade jupyterlab jupyterlab-git
RUN jupyter lab build

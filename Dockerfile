# image for portfolio
FROM CentOS:7
MAINTAINER wwy version: 0.1

ENV LD_LIBRARY_PATH=/usr/local/lib

COPY ./sources.list /etc/apt/
RUN depends='make r-base r-base-dev' &&\
    apt-get update &&\
    apt-get install -y $depends

#anaconda
COPY ./Anaconda2-4.2.0-Linux-x86_64.sh /tmp/
RUN bash /tmp/Anaconda2-4.2.0-Linux-x86_64.sh -b
ENV PATH /root/anaconda2/bin:$PATH

#ta-lib
COPY ./ta-lib-0.4.0-src.tar.gz /tmp/
RUN cd /tmp &&\
    tar -xzf ta-lib-0.4.0-src.tar.gz &&\
    cd /tmp/ta-lib &&\
    ./configure &&\
    make &&\
    make install

#pip
COPY ./pip.conf /root/.config/pip/
COPY ./SuiteSparse-4.5.3.tar.gz /tmp/
ENV CVXOPT_SUITESPARSE_SRC_DIR=/tmp/SuiteSparse
RUN cd /tmp &&\
    tar xzf SuiteSparse-4.5.3.tar.gz &&\
    pip install celery flasgger flask rpy2 arch pymongo grpc protobuf cvxopt ta-lib grpcio seaborn

#Qi4Trade
COPY Qi4Trade /tmp/Qi4Trade
RUN cd /tmp/Qi4Trade/trunk &&\
    python setup.py install

#SITxuk
COPY SITxuk /tmp/SITxuk
RUN cd /tmp &&\
    R CMD build SITxuk &&\
    R CMD INSTALL SITxuk_0.1.0.tar.gz

#ndparser
COPY ndparser.so /root/anaconda2/lib/python2.7/site-packages/
COPY ndparser-1.0-py2.7.egg-info /root/anaconda2/lib/python2.7/site-packages/

#clear
RUN apt-get purge -y --auto-remove make &&\
    apt-get clean &&\
    rm -rf /tmp/* &&\
    rm -rf /var/lib/apt/lists/*

#porfolio-web
COPY portfolio-web /root/portfolio-web
COPY libgomp.so.1.0.0 /root/anaconda2/lib/
ENV FLASK_SETTINGS=/root/portfolio-web/trunk/api/dev
ENV PYTHONPATH=/root/portfolio-web/trunk
WORKDIR /root/portfolio-web/trunk
EXPOSE 8686
CMD ["python","api/server.py"]

# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini
ENTRYPOINT ["/usr/bin/tini", "--"]
EXPOSE 8888
CMD ["jupyter","notebook","--port=8888","--no-browser","--ip=0.0.0.0"]
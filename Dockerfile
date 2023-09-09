FROM registry.access.redhat.com/ubi8/python-311:latest
USER root
RUN dnf -y install make gcc libtool
USER 1001

RUN wget https://github.com/VirusTotal/yara/archive/refs/tags/v4.3.2.tar.gz
RUN tar -zxf v4.3.2.tar.gz
WORKDIR /opt/app-root/src/yara-4.3.2
RUN ./bootstrap.sh
RUN ./configure
RUN make
USER root
RUN make install

# RUN ln -s /usr/local/lib/libyara.so /opt/app-root/lib/libyara.so
RUN cp -r /usr/local/lib/* /opt/app-root/lib/
USER 1001
WORKDIR /opt/app-root/src
RUN git clone https://github.com/reversinglabs/reversinglabs-yara-rules.git 
ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
ADD compile-rules.py compile-rules.py 
RUN python3 compile-rules.py /opt/app-root/src/reversinglabs-yara-rules

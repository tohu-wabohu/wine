# FTP

## Explicit FTPS (FTPES)
Explicit FTPS (FTPES) is the newer method of FTPS transfer and has generally overtaken implicit FTPS use, with the exception of legacy systems. When explicit FTPS is used, a traditional FTP connection is established on the same standard port as FTP. Once the connection is made (before login), a secure SSL connection is established via port 21. Today, explicit FTPS (also FTPES) is supported by the majority of FTP servers since it is an approved, standard way of protecting data.

## Implicit FTPS
Implicit FTPS was the first method created to encrypt data sent "via FTP"; although a different port is used. When using implicit FTPS, an SSL connection is immediately established via port 990 before login or file transfer can begin. Implicit FTPS is considered a deprecated protocol, meaning that it not the current standard.

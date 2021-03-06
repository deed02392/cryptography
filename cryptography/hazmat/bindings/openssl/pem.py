# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import, division, print_function

INCLUDES = """
#include <openssl/pem.h>
"""

TYPES = """
typedef int pem_password_cb(char *buf, int size, int rwflag, void *userdata);
"""

FUNCTIONS = """
X509 *PEM_read_bio_X509(BIO *, X509 **, pem_password_cb *, void *);
int PEM_write_bio_X509(BIO *, X509 *);

int PEM_write_bio_PrivateKey(BIO *, EVP_PKEY *, const EVP_CIPHER *,
                             unsigned char *, int, pem_password_cb *, void *);

EVP_PKEY *PEM_read_bio_PrivateKey(BIO *, EVP_PKEY **, pem_password_cb *,
                                 void *);

int PEM_write_bio_PKCS8PrivateKey(BIO *, EVP_PKEY *, const EVP_CIPHER *,
                                  char *, int, pem_password_cb *, void *);
int PEM_write_bio_PKCS8PrivateKey_nid(BIO *, EVP_PKEY *, int, char *, int,
                                      pem_password_cb *, void *);

int i2d_PKCS8PrivateKey_bio(BIO *, EVP_PKEY *, const EVP_CIPHER *,
                            char *, int, pem_password_cb *, void *);
int i2d_PKCS8PrivateKey_nid_bio(BIO *, EVP_PKEY *, int,
                                char *, int, pem_password_cb *, void *);

EVP_PKEY *d2i_PKCS8PrivateKey_bio(BIO *, EVP_PKEY **, pem_password_cb *,
                                  void *);

int PEM_write_bio_X509_REQ(BIO *, X509_REQ *);

X509_REQ *PEM_read_bio_X509_REQ(BIO *, X509_REQ **, pem_password_cb *, void *);

X509_CRL *PEM_read_bio_X509_CRL(BIO *, X509_CRL **, pem_password_cb *, void *);

int PEM_write_bio_X509_CRL(BIO *, X509_CRL *);

PKCS7 *PEM_read_bio_PKCS7(BIO *, PKCS7 **, pem_password_cb *, void *);
DH *PEM_read_bio_DHparams(BIO *, DH **, pem_password_cb *, void *);

DSA *PEM_read_bio_DSAPrivateKey(BIO *, DSA **, pem_password_cb *, void *);

RSA *PEM_read_bio_RSAPrivateKey(BIO *, RSA **, pem_password_cb *, void *);

int PEM_write_bio_DSAPrivateKey(BIO *, DSA *, const EVP_CIPHER *,
                                unsigned char *, int,
                                pem_password_cb *, void *);

int PEM_write_bio_RSAPrivateKey(BIO *, RSA *, const EVP_CIPHER *,
                                unsigned char *, int,
                                pem_password_cb *, void *);

DSA *PEM_read_bio_DSA_PUBKEY(BIO *, DSA **, pem_password_cb *, void *);

RSA *PEM_read_bio_RSAPublicKey(BIO *, RSA **, pem_password_cb *, void *);

int PEM_write_bio_DSA_PUBKEY(BIO *, DSA *);

int PEM_write_bio_RSAPublicKey(BIO *, const RSA *);

EVP_PKEY *PEM_read_bio_PUBKEY(BIO *, EVP_PKEY **, pem_password_cb *, void *);
int PEM_write_bio_PUBKEY(BIO *, EVP_PKEY *);
"""

MACROS = """
"""

CUSTOMIZATIONS = """
"""

CONDITIONAL_NAMES = {}

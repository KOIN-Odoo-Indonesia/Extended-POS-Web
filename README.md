# Extended-POS-Web

Proyek ini merupakan proyek komunitas Odoo Indonesia untuk menjawab beberapa kebutuhan penggunan teknologi asynchronous yang sesuai dengan ekspektasi bersama untuk menampung data yang intensif dan sifatnya bisa offline / online

Tahap Pertama tujuan dari add ons ini untuk mengganti local storage odoo pos existing diganti menggunakan teknologi couchbase. 

Requirement untuk testing-nya :
- odoo13 community edition
- point_of_sales addons odoo13
- Couchdb di server yang akan digunakan sebagai odoo server.

Tambahan :
setelah setup couchdb pastikan untuk allow CORS di server couchdb.
Caranya :
1. https://pouchdb.com/guides/setup-couchdb.html#set-up-cors
2. Aktifkan CORS didalam console couchdb


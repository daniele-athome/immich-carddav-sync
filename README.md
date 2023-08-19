Immich CardDAV sync tool
========================

Work in progress. Stay tuned.

* vdir somewhere
* request all people to immich
* loop and search in vdir
  * if name match and has BDAY, call immich update person

Issues:

* duplicate people in immich should all have the same birthdate set
* duplicate contacts should be selected interactively or beforehand via parameter (e.g. fail)

Contacts fetching:

* using vdirsyncer now, could be enough to implement CardDAV just to download a whole address book on start

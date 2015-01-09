SLDB Documentation
==================
The SimLab Database (SLDB) package is a Python module that facilitate efficient
storage and analysis of high-throughput B- and T-cell sequence data.  It's
primary goals are to:

- **Reduce ad-hoc scripting:** Analysis is often done on an ad-hoc basis as
  the need for data is realized, requiring specialized scripts to be written.
  SLDB provides a large set of analytical data for sequences immediately and for
  specialized analysis, robust export functionality.

- **Minimize flat-files:** Flat files are currently the standard method of
  exchanging data in the biological sciences.  There are a myriad of drawbacks
  when using these including a lack of `referential integrity
  <http://en.wikipedia.org/wiki/Referential_integrity>`_, unclear `provenance
  <http://en.wikipedia.org/wiki/Provenance#Data_provenance>`_, and
  non-standardized formats.
  
  SLDB eliminates these through the use of an industry-leading database, MySQL,
  and strong data guarantees.  When data must be exchanged as a flat-file, many
  export options, including FASTA and tab-delineation, are available.

- **Provide a generic API:** SLDB provides both a REST API for language-agnostic
  database querying as well as a suite of Python classes for interacting directly
  with the database for customized querying.

SLDB has three primary components:

- **Clonal identification pipeline:** A series of steps which take as input raw
  sequences in FASTA format, identifies V- and J-genes (as well as many other
  features) and subsequently groups sequences from the same subject into clones.

- **Analysis framework:** A module that provide detailed analysis of sequences.
  This includes mutation analysis, gene utilization breakdowns, and feature
  distributions  (e.g. CDR3 length, V-gene utilization).

- **API:**  SLDB includes two APIs.  First, the REST
  API allows other application and websites (via AJAX) to interact with the
  underlying database without writing any database specific code.  Further, the
  REST API is language agnostic, using HTTP to exchange data.

  Second is the Python API which implements the data models and querying
  functionality.  This allows developers to write customized queries directly
  interacting with the database.

Each of the components can be used independently so long as the underlying
database is properly populated.  For example, custom clonal identification can
be used prior to analysis if desired.

Underlying Technologies
-----------------------

- `MySQL <http://www.mysql.com>`_: The database (agnostic
  of implementation like `MariaDB <https://mariadb.org>`_) which enforces rigorous
  data guarantees, indexes the data for fast retrieval, and enforces atomicity
  of operations

- `TokuDB <http://www.tokutek.com/tokudb-for-mysql>`_: The storage engine which
  writes the database to non-volatile media, and is optimized for large quantities
  of data such as that in high-throughput sequencing.

- `SQLAlchemy <http://www.sqlalchemy.org>`_: The interface between Python and
  the database which abstracts SQL queries from the implementation and enforces
  the data model within Python.

- `Bottle <http://bottlepy.org>`_: A lightweight web-framework for Python which
  serves content via the REST API allowing web-applications to issue AJAX requests
  to the SLDB framework.


Modules
====================
.. toctree::
    :maxdepth: 2

    common
    models
    api

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
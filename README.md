# olam-ml-en
API written in Flask to find English meaning for a Malayalam word. This API uses Olam [dictionary](https://olam.in/open/enml/)


Requirements
=========================
* [MongoDB](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)
* Python

Install
=========================

```bash
$ git clone https://github.com/sreecodeslayer/olam-ml-en.git
$ cd olam-ml-en
$ pip install -r requirements.txt
$ python app.py
```
> Also, if your MongoDB is having Auth, please provide the auth uri for MongoClient in `app.py`, see [here](http://api.mongodb.com/python/current/examples/authentication.html)

Usage
=========================
Send GET request as  

`http://127.0.0.1:1122/search?text=കാര്യം`  
will give a `JSON` output as:  

```json
{
  "result": [
    "Tender spot", 
    "Thing", 
    "Turn", 
    "Problem", 
    "Proceeding", 
    "Purpose", 
    "Pursuit", 
    "Question", 
    "Relation", 
    "Requirement", 
    "In case", 
    "Item", 
    "Matter", 
    "Pace", 
    "Part", 
    "Particular", 
    "Point", 
    "Act", 
    "Affair", 
    "Business", 
    "Concern", 
    "Deed", 
    "Fact", 
    "Factor"
  ]
}
```

or 

`http://127.0.0.1:1122/search?text=നിറഞ്ഞു വഴിയുന്ന`  
will give a `JSON` output as:  

```json
{
  "result": [
    "Profuse"
  ]
}
```
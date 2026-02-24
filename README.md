# xcli

Small terminal tool to browse Nutanix resources and quickly get their UUIDs.
I built this because I was spending too much time looking for UUIDs when working with Ansible, Terraform and Nutanix SSP.
Shared it with my team and they found it useful, so I’m putting it here as well.

---

**What it does**

Lets you browse:
* VMs
* Images
* Subnets
* Containers
* Nutanix Categories
* Prism Central
* Prism Element

And shows the UUID instantly in the terminal.

---

**Tested on**
* prism central 7.5
* AOS 7.5
* AHV 11.0
**How to use it**

clone this repo:

```
git clone https://github.com/elyacoub9/xcli.git
```

Install deps:

```
pip install -r requirements.txt
```
---

create `config.py` file and add:

```
HOST = "<pc-ip>"
USERNAME = "admin"
PASSWORD = "password"
```
---

Run
```bash
python xcli.py
```
---

Feedback is welcome.

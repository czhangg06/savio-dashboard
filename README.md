# savio-dashboard

Web interface to the UC Berkeley **Savio** cluster.

## 1. Overview

Savio is a high performance computing cluster maintained by Berkeley Research Computing (BRC) and Lawrence Berkeley National Laboratory (LBNL) at the University of California, Berkeley.

The Savio-centric dashboard seeks to provide additional functionality to the current SLURM scheduler banking system by allowing administrative users to allocate a certain amount of compute time to each user under his account. Other features of the Savio-centric dashboard allow users to graphically view statistics from compute time usage and job history to better adjust their usage rate in the future. Overall, this dashboard seeks to provide greater functionality as well as a more intuitive, user-friendly experience for high performance computing researchers at UC Berkeley.

## 2. How to run

```
    $ python manage.py runserver
```

List of package dependencies / extra components to use this dashboard:

- **Savio** account as faculty, staff, or student researcher at UC Berkeley
- **DjangoDB** (?)
- **Python3.5+** (?) or is this **Python2.7+**

## 3. To Do

**C** = Cassie
**O** = Oliver

- [ ] O: creates template of how to make *pretty* mouse-over event for text
- [ ] O: adds .gitignore file
- [ ] C: ask about LICENSE.txt  + create
- [ ] O + C: add requirements.txt
- [ ] O + C: add setup.py **(? is this part needed ?)**

- [x] C: notification center (getting notif to display, formatting notif, marking read vs. unread)
- [ ] C: notification center (displaying date, registering when to send)
- [ ] C: statistics (displaying graphs via d3, smooth transition b/w graphs, formatting job history chart + filters)
- [ ] C: quota manager (displaying user list, filters, displaying graph)
- [ ] C: su calculator 
- [ ] C: FAQs (figure out important questions, when to redirect to another page, how to display information)
- [ ] C: settings (allow update email settings)
- [ ] C: configure with backend API
- [ ] C: deploy in Pheonix

## 4. (Cassie's) issues

Currently none (other than what I've already commmunicated!)

Pundit - ITTT for python
------------------

Pundit is a ITTT (If This Then That) for python, where decision is made according to 
the conditions specified and gives you what you expect. Pundit supports string type,
integer
 
 
## Documentation

### Installation

```bash
pip install pundit
```


## Basic Usages

#### Set Structure for Input

```python
from pundit import PunditBase
base = PunditBase()

#### Usage

base.add_structure(arg_1, arg_2)
```

#### Set conditiongroup

```python
from pundit import Conditiongroup
conditiongroup = Conditiongroup()

#### Usage

conditiongroup.add_condition(match, condition type, success response, failed response)
```

**Match:** str or integer data argument

**Condition Types:** 
```
String
IN
NOT_IN
NOT_IS

Integer
EQ
NOT_EQ
GT
LT
GTE
LTE

List
IN
ORDER_IS
VALUE_IS

Dictionary
VALUE_IS
KEY_IS
KEY_IN
KEY_NOT_IN
```


#### Evaluate pundit

```python
from pundit import Pundit
pundit = Pundit(base, conditiongroup)
```
>>> pundit.evaluate(input)





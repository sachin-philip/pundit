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
from pundit.base import PunditBase
base = PunditBase()

#### Usage

base.add_structure(arg_1, arg_2)
```

#### Set conditiongroup

```python
from pundit.condition import Conditiongroup
conditiongroup = Conditiongroup()

#### Usage

conditiongroup.add_condition(match, condition type, argument, success response, failed response)
```

**Match:** str or integer data argument
**Argument:** arguments arg_1, arg_2 which was set as structure

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

```


#### Evaluate pundit

```python
from pundit import Pundit
pundit = Pundit(base, conditiongroup)


>>> pundit.evaluate(input_1, input_2)
```
**input** Input to evaluate




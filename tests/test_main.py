**Pytest uchun test kodini quyidagicha yozing:**

```python
import pytest
from atm import ATM

def test_atm_init():
    atm = ATM(1000)
    assert atm.balance == 1000

def test_withdraw():
    atm = ATM(1000)
    atm.withdraw(500)
    assert atm.balance == 500

def test_withdraw_insufficient_funds():
    atm = ATM(1000)
    with pytest.raises(ValueError):
        atm.withdraw(1500)

def test_deposit():
    atm = ATM(1000)
    atm.deposit(500)
    assert atm.balance == 1500

def test_balance():
    atm = ATM(1000)
    assert atm.balance == 1000

def test_withdraw_zero():
    atm = ATM(1000)
    atm.withdraw(0)
    assert atm.balance == 1000
```

**Jest uchun test kodini quyidagicha yozing:**

```javascript
import { ATM } from './atm';

describe('ATM', () => {
  it('should initialize with correct balance', () => {
    const atm = new ATM(1000);
    expect(atm.balance).toBe(1000);
  });

  it('should withdraw correctly', () => {
    const atm = new ATM(1000);
    atm.withdraw(500);
    expect(atm.balance).toBe(500);
  });

  it('should throw error for insufficient funds', () => {
    const atm = new ATM(1000);
    expect(() => atm.withdraw(1500)).toThrowError();
  });

  it('should deposit correctly', () => {
    const atm = new ATM(1000);
    atm.deposit(500);
    expect(atm.balance).toBe(1500);
  });

  it('should return correct balance', () => {
    const atm = new ATM(1000);
    expect(atm.balance).toBe(1000);
  });

  it('should not change balance for zero withdrawal', () => {
    const atm = new ATM(1000);
    atm.withdraw(0);
    expect(atm.balance).toBe(1000);
  });
});
```

# WAR DOG TORMENTITE
```statblock
name: "WAR DOG TORMENTITE"
level: 5
roles:
  - BAND
  - HEXER
ancestry:
  - Humanoid
  - War
  - Dog
ev: 7
stamina: 30
speed: 5
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - +0
  - +0
  - +2
  - +3
  - +0
actions:
  - name: "Mark of Agony"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 corruption damage
      <br />★ 12–16 8 corruption damage; marked (save ends)
      <br />✸ 17+ 9 corruption damage; marked (save ends) 
      <br />**Effect:** Strikes against marked targets have an edge. Whenever the tormentite takes damage, each marked target takes 3 damage."
  - name: "Vortex of Pain"
    desc:
      "
      <br />**Keywords** Area, Magic
      <br />**Distance** 4 cube within 10
      <br />**Target** All enemies
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 corruption damage
      <br />★ 12–16 4 corruption damage
      <br />✸ 17+ 5 corruption damage; an ally within the affected area can end one save ends effect affecting them and give it to a target. 
      <br />**Effect:** The tormentite regains 2 stamina per target of this ability."
traits:
  - name: "Persistent Pain" 
    desc: "The tormentite takes 1 damage at the start of each of their turns."
  - name: "Loyalty Collar"
    desc: "When the tormentite dies, they explode, dealing 2d6 damage to each adjacent enemy."

```

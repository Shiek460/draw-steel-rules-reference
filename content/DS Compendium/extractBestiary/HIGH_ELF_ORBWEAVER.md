# HIGH ELF ORBWEAVER
```statblock
name: "HIGH ELF ORBWEAVER"
level: 3
roles:
  - PLATOON
  - HEXER
ancestry:
  - Fey
  - High
  - Elf
  - Humanoid
ev: 10
stamina: 40
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - 0
  - 0
  - +2
  - +2
  - +2
actions:
  - name: "Awash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 cube within 1
      <br />**Target** All creatures in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 cold damage; M< 0 push 3
      <br />★ 12–16 6 cold damage; M< 1 push 5 or [[prone]]
      <br />✸ 17+ 9 cold damage; M< 2 slide 5 or [[prone]]"
  - name: "Aetherweb"
    desc:
      "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 8
      <br />**Target** 2 enemies or objects
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; R< 0 [[slowed]] (save ends)
      <br />★ 12–16 8 damage; R< 1 [[slowed]] (save ends)
      <br />✸ 17+ 11 damage; R< 2 [[restrained]] (save ends) 
      <br />**Effect:** Each enemy within 3 of a target suffers the same additional effects as the target unless they shift into an unoccupied square adjacent to them"
traits:
  - name: "Otherworldly Grace"
    desc: "At the start of their turn, the dawn mage can turn the duration of one save ends effect they suffer from into EoT."

```

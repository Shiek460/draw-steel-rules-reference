# WODE ELF DRUID
```statblock
name: "WODE ELF DRUID"
level: 2
roles:
  - PLATOON
  - CONTROLLER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 8
stamina: 30
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +1
  - 0
  - 0
  - +2
actions:
  - name: "Entangling Vines"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; pull 1
      <br />★ 12–16 8 damage; pull 3; M< 1 [[slowed]] (save ends)
      <br />✸ 17+ 10 damage; pull 5; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A creature [[slowed]] by this ability can’t search for hidden creatures until the condition ends. 
      <br />**3 Malice** The area of the cube and the potency of the effect both increase by 1."
maneuvers:
  - name: "The Wode Protects Us"
    desc: "
      <br />**Cost** 3 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self and Ranged 5
      <br />**Target** Self and 3 allies 
      <br />**Effect:** Each target teleports to a square within 10 that has cover or concealment from all enemies."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

```

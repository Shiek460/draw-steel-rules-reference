# WODE ELF SENTRY
```statblock
name: "WODE ELF SENTRY"
level: 1
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 6
stamina: 30
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +2
  - 0
  - 0
  - +1
actions:
  - name: "Tracer Longbow"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage
      <br />✸ 17+ 9 damage; marked (save ends) 
      <br />**Effect:** Each ally has an edge on strikes and abilities against marked targets until the condition ends.
      <br />**3 Malice** The sentry targets two additional creatures or objects."
maneuvers:
  - name: "Death Blossom"
    desc: "
      <br />**Cost** 2 Malice
      <br />**Keywords** Area, Weapon
      <br />**Distance** 5 burst
      <br />**Target** All marked enemies 
      <br />**Effect:** 3 damage."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

```

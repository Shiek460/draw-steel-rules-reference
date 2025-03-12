# WODE ELF GREEN SEER
```statblock
name: "WODE ELF GREEN SEER"
level: 1
roles:
  - PLATOON
  - HEXER
ancestry:
  - Fey
  - Humanoid
  - Wode
  - Elf
ev: 6
stamina: 20
speed: 7
size: 1M /
stability: 0
free_strike: 3
characteristics:
  - 0
  - +1
  - 0
  - +2
  - +1
actions:
  - name: "The Forest’s Embrace"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 1 creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage
      <br />★ 12–16 7 damage; I< 1 [[restrained]] (save ends)
      <br />✸ 17+ 9 damage; I< 2 [[restrained]] (save ends) 
      <br />**Effect:** A creature [[restrained]] by this ability can’t search for hidden creatures until the condition ends."
maneuvers:
  - name: "The Natural Cycle"
    desc: "
      <br />**Keywords** Magic, Ranged
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 2 damage
      <br />★ 12–16 4 damage; P< 1 target has a double bane on strikes (save ends)
      <br />✸ 17+ 6 damage; P< 2 [[bleeding]] (save ends), target has a double bane on strikes (save ends) 
      <br />**Effect:** The green seer causes lichen to form and encroach upon each target. "
ta:
  - name: "Foreseen Punishment (Free Triggered Action)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature uses a triggered action targeting the green seer or an ally within distance. 
      <br />**Effect:** The green seer makes a free strike against the target."
traits:
  - name: "Masking Glamor"
    desc: "The elf immediately hides at the end of their turn while in cover or concealment, even if they are observed."

```

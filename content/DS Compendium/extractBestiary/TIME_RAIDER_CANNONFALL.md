# TIME RAIDER CANNONFALL
```statblock
name: "TIME RAIDER CANNONFALL"
level: 3
roles:
  - PLATOON
  - ARTILLERY
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 40
immunities: Psychic 3
speed: 5
size: 1L /
stability: 3
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +0
actions:
  - name: "Sunderbuss"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Psionic, Ranged, Weapon
      <br />**Distance** 3 cube within 10
      <br />**Target** All enemies in the cube
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 sonic damage
      <br />★ 12–16 7 sonic damage
      <br />✸ 17+ 10 sonic damage; [[prone]]; M< 2 [[slowed]] (save ends) 
      <br />**Effect:** A layer of ground or floor beneath the area that is 1 square deep is destroyed."
ta:
  - name: "Buss Buffer (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Psionic
      <br />**Distance** Self and 5 burst
      <br />**Target** Self and all allies in the burst 
      <br />**Trigger** A creature damages the cannonfall with a ranged or area ability. 
      <br />**Effect:** The damage is reduced by half for the cannonfall and each target also affected by the triggering ability."
traits:
  - name: "Foresight"
    desc: "The cannonfall doesn’t have a bane on strikes against concealed creatures."

```

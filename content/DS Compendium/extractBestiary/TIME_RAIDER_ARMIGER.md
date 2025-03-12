ra# TIME RAIDER ARMIGER
```statblock
name: "TIME RAIDER ARMIGER"
level: 3
roles:
  - PLATOON
  - DEFENDER
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 60
immunities: Psychic 3
speed: 5
size: 1M /
stability: 0
free_strike: 5
characteristics:
  - +0
  - +2
  - +2
  - +2
  - +0
actions:
  - name: "Serrated Saber"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** One creature or object
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 7 damage
      <br />★ 12–16 10 damage
      <br />✸ 17+ 13 damage; R< 2 [[weakened]] (save ends) 
      <br />**2 Malice** A creature is [[bleeding]] while [[weakened]] from this ability."
ta:
  - name: "Shared Sickness"
    desc: "
      <br />**Keywords** Psionic, Ranged
      <br />**Distance** Ranged 20
      <br />**Target** Triggering creature 
      <br />**Trigger** A creature deals damage to any ally of the armiger to whom the armiger has [[Line of Effect]].
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 4 psychic damage; R< 0 5 poison damage
      <br />★ 12–16 6 psychic damage; R< 1 5 poison damage
      <br />✸ 17+ 9 psychic damage; R< 2 5 poison damage"
traits:
  - name: "Foresight"
    desc: "The armiger doesn’t have a bane on strikes against concealed creatures."
  - name: "Kuran’zoi Heraldry"
    desc: "While any time raider starts their turn with [[Line of Effect]] to the armiger, that time raider can end one condition affecting them."

```

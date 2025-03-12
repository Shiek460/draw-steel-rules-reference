# TIME RAIDER VERTEX
```statblock
name: "TIME RAIDER VERTEX"
level: 3
roles:
  - PLATOON
  - SUPPORT
ancestry:
  - Humanoid
  - Time
  - Raider
ev: 10
stamina: 50
immunities: Psychic 3
speed: 5 (fly, hover)
size: 2 /
stability: 3
free_strike: 5
characteristics:
  - +1
  - +1
  - +2
  - +1
  - +0
actions:
  - name: "Psionic Slam"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Psionic, Strike
      <br />**Distance** Reach 2
      <br />**Target** One creature
      <br />`dice: 2d10 + 2`
      <br />✦ ≤11 5 damage; 2 psychic damage
      <br />★ 12–16 7 damage; 3 psychic damage
      <br />✸ 17+ 9 damage; 4 psychic damage 
      <br />**Effect:** Power rolls made against the target have an edge until the start of the vertex’s next turn."
  - name: "Split Space"
    desc:
      "<br />**Cost** 5 Malice
      <br />**Keywords** Area, Psionic, Ranged
      <br />**Distance** 2 cube within 10
      <br />**Target** Special 
      <br />**Effect:** A portal fills the area, leading to a location the vertex has experienced (in person or otherwise) on any plane of existence. Each creature who touches the portal is instantly teleported to the nearest unoccupied square at the chosen location. The portal lasts until the vertex dies, uses this ability again, dismisses the portal (no action required), or is transported by the portal."
maneuvers:
  - name: "Invigorated March"
    desc: "
      <br />**Keywords** Area, Psionic
      <br />**Distance** 4 burst
      <br />**Target** All allies in the burst 
      <br />**Effect:** Each target shifts up to half their speed."
traits:
  - name: "Foresight"
    desc: "The vertex doesn’t have a bane on strikes against concealed creatures."

```

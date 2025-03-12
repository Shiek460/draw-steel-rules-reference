# SHAMBLING MOUND
```statblock
name: "SHAMBLING MOUND"
level: 5
roles:
  - SOLO
ancestry:
  - Plant
  - Shambling Mound
ev: 70
stamina: 400
speed: 3
size: 3 /
stability: 5
free_strike: 7
characteristics:
  - +4
  - −1
  - +0
  - +1
  - +0
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The shambling mound takes 2 turns each round. They can use two actions on each of their turns and can take each turn after an enemy turn they choose. While [[dazed]], the shambling mound can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the shambling mound can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Engulfing Sack"
    desc: "The shambling mound has a vegetative sack on their body where they carry engulfed creatures. The sack has 30 stamina, damage immunity 5, and fire weakness 10. Destroying the sack frees creatures trapped by the shambling mound’s Engulf action. The shambling mound regrows the sack at the beginning of their next turn."
actions:
  - name: "Vine Lash"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 6
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; A< 3 [[grabbed]]
      <br />★ 12–16 16 damage; A< 4 [[grabbed]]
      <br />✸ 17+ 19 damage; [[grabbed]] 
      <br />**2 Malice** The shambling mound can slide one or both targets up to 6 squares. 
      <br />**3 Malice** Each target takes 7 poison damage."
  - name: "Seismic Slam"
    desc:
      "
      <br />**Keywords** Area, Weapon
      <br />**Distance** 6 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 damage; M< 2 [[dazed]] (save ends)
      <br />★ 12–16 6 damage; M< 3 [[dazed]] (save ends)
      <br />✸ 17+ 7 damage; M< 4 [[dazed]] (save ends)"
  - name: "Engulf"
    desc:
      "<br />**Cost** 2 Malice
      <br />**Keywords** Area, Melee
      <br />**Distance** Melee 6
      <br />**Target** 1 creature or object 
      <br />**Effect:** The shambling mound reaches out with writhing vines and A< 3 engulfs an enemy size 1L or smaller into their sack. The potency increases by 1 if the target is [[grabbed]] by the shambling mound. An engulfed creature is [[restrained]], takes 3 poison damage at the start of each turn of combat, and can’t take damage from abilities used from outside the sack. When the shambling mound moves, the engulfed creature moves with them. If the mound dies or their engulfing sack is destroyed, each engulfed creature is freed and shunted to an unoccupied square within 2 squares. 2+ Malice The shambling mound can engulf 1 additional enemy for every 2 malice spent."
maneuvers:
  - name: "Leech"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Each creature trapped by Engulf 
      <br />**Effect:** 5 poison damage. The shambling mound gains 5 temporary stamina for each creature affected by this maneuver." 
ta:
  - name: "Tether Down"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 6
      <br />**Target** One creature 
      <br />**Trigger** A creature within distance moves.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 damage; M< 2 [[restrained]] (EoT)
      <br />★ 12–16 12 damage; M< 3 [[restrained]] (EoT)
      <br />✸ 17+ 15 damage; M< 4 [[restrained]] (EoT)"
traits:
  - name: "False Appearance"
    desc: "While the shambling mound remains motionless, they are indistinguishable from ordinary vegetation."
  - name: "Frothing Flora"
    desc: "The area within 6 squares of the shambling mound is considered difficult terrain."
  - name: "Ravenous Overgrowth (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 10 x 2 line within 1
      <br />**Target** All creatures in the line
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 7 damage, pull 3
      <br />★ 12–16 12 damage; pull 4; targets gain poison weakness 3 until the encounter ends
      <br />✸ 17+ 15 damage; pull 6; targets gain poison weakness 5 until the encounter ends"
  - name: "Composting (Villain Action 2)"
    desc: "
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** Melee 6
      <br />**Target** All enemies 
      <br />**Effect:** The shambling mound attempts to devour each enemy within distance with its Engulf action without spending malice."
  - name: "Exposed Crux (Villain Action 3)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The shambling mound rips themself apart to lay waste, exposing the crux of magic holding them together. The distance of the shambling mound’s melee abilities increases to 10, they have a double edge on power rolls, and strikes have an edge against them."

```

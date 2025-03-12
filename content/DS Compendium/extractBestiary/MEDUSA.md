# MEDUSA
```statblock
name: "MEDUSA"
level: 5
roles:
  - SOLO
ancestry:
  - Accursed
  - Humanoid
  - Medusa
ev: 70
stamina: 400
immunities: Poison 5, Acid 5
speed: 5
size: 1M /
stability: 0
free_strike: 7
characteristics:
  - +2
  - +4
  - +0
  - +0
  - +0
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The medusa takes 2 turns each round. They can use two actions on each of their turns and can take each turn after an enemy turn they choose. While [[dazed]], the medusa can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the medusa can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
actions:
  - name: "Snake Bite"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 1
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[slowed]] (save ends)
      <br />★ 12–16 16 damage; M< 3 [[slowed]] (save ends)
      <br />✸ 17+ 19 damage; M< 4 [[slowed]] (save ends)"
  - name: "Damning Gaze"
    desc:
      "
      <br />**Keywords** Magic, Ranged, Strike
      <br />**Distance** Ranged 10
      <br />**Target** 2 creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; push 3
      <br />★ 12–16 16 damage; push 5
      <br />✸ 17+ 19 damage; push 7 3 Malice The medusa targets two additional creatures or objects."
  - name: "Petrify"
    desc: "
      <br />**Cost** 5 Malice
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each enemy in the burst 
      <br />**Effect:** The medusa turns dozens of eerie snake eyes on their foes. Each target must make a Might test. A target with cover has an edge on the test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 [[slowed]] (save ends) or M< 4 [[restrained]] (save ends)
      <br />★ 12–16 M< 3 [[restrained]] (save ends)
      <br />✦ 17+ M< 2 [[restrained]] (save ends) 
      <br />**Effect:** An already [[slowed]] target has -1 to resist the potency. A target [[restrained]] by this ability magically begins to turn to stone. A target that ends two consecutive turns [[restrained]] by this ability is petrified (see Petrification)."
maneuvers:
  - name: "Nimble Escape"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The medusa shifts 3 and hides, even if observed."
ta:
  - name: "Venomous Spit"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Melee 1
      <br />**Target** One creature 
      <br />**Trigger** A creature deals damage to the medusa.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 13 acid damage
      <br />★ 12–16 18 acid damage
      <br />✸ 17+ 22 acid damage"
traits:
  - name: "Cunning Edge"
    desc: "The medusa has an edge on power rolls made against any creature affected by their Petrify ability."
  - name: "Many Peering Eyes"
    desc: "The medusa can’t be flanked."
  - name: "Mass Petrify (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic, Ranged
      <br />**Distance** [[Line of Effect]]
      <br />**Target** All enemies 
      <br />**Effect:** The medusa uses their Petrify ability against each target without spending Malice. Each target not behind cover has a bane on the test."
  - name: "Serpent Wings (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** The medusa manifests temporary wings and vertically shifts up to their speed. During or after this movement, they can use Snake Bite and Damning Gaze once each."
  - name: "Stone Puppets (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 10 burst
      <br />**Target** Special 
      <br />**Effect:** Each stone statue and creature affected by Petrify within distance moves up to their speed and uses a signature action with an edge targeting an enemy of medusa’s choice as a free triggered action. A stone statue without its own stats has a speed of 5 and uses the Medusa’s free strike instead."

```

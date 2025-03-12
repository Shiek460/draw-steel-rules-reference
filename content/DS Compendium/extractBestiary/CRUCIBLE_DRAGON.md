# CRUCIBLE DRAGON
```statblock
name: "CRUCIBLE DRAGON"
level: 6
roles:
  - SOLO
ancestry:
  - Dragon
  - Elemental
ev: 80
stamina: 450
immunities: fire 6
speed: 8
size: 4 /
stability: 6
free_strike: 7
characteristics:
  - +4
  - -1
  - +3
  - +3
  - +2
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The dragon takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the dragon can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the dragon can take 10 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Magnetized Wyrmscale Aura"
    desc: "The dragon’s scales emit a 3 aura of magnetism that affects metal equipment and objects A creature that enters an affected square or starts their turn there while slagged or wearing metal is pulled 2 towards the dragon and is M< 3 unable to move away."
  - name: "Crucible Dragon’s Domain"
    desc: "If the encounter map is a location the dragon has occupied for 1 week or more, melted metal and blades coat nearly every wall and column. A creature or object other than the dragon that comes into physical contact with an affected surface takes 5 damage. Whenever an enemy uses an ability that deals electric damage, they take 1d6 damage and deal half the amount of damage to each adjacent enemy and object."
actions:
  - name: "Slag Spew"
    desc: "
      <br />**Type:** Signature
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 10 × 2 line within 1
      <br />**Target** All creatures and objects 
      <br />**Effect:** Each target makes an Might test.
      <br />✸ ≤11 13 fire damage; A< 4 slagged (save ends)
      <br />★ 12–16 10 fire damage; A< 3 slagged (save ends)
      <br />`dice: 2d10 + 4`
      <br />✦ 17+ 6 fire damage; A< 2 slagged (save ends) 
      <br />**Effect:** Until the condition ends, a slagged target is coated in molten metal, takes 2d6 fire damage at the start of each of their turns, and is M< 3 [[restrained]] (save ends) whenever they take cold damage."
  - name: "Forge Hammer Tail Slam"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 3
      <br />**Target** Two creatures or objects
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 11 damage; M< 2 [[prone]]
      <br />★ 12–16 17+ damage; M< 3 [[prone]]
      <br />✸ 17+ 20 damage; M< 4 [[prone]] 
      <br />**Effect:** The dragon makes a free strike against each slagged target knocked [[prone]] by this ability. 
      <br />**1 Malice** The hammerhead freezes, dealing 1d6 cold damage."
maneuvers:
  - name: "Thermodynamic Flight"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** Area, Melee
      <br />**Distance** 2 burst
      <br />**Target** All enemies in the burst 
      <br />**Effect:** The dragon expels blistering steam straight down, dealing 7 fire damage to each target. The dragon then shifts up to their speed vertically and adds the fly keyword to their movement until the end of the round."
  - name: "Heat Buffer (Free Maneuver)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self (while flying)
      <br />**Target** Self 
      <br />**Effect:** The dragon can use this ability once per round. They continue to give off steam to extend the duration of their flight for an additional round. Each creature under the dragon when they use this ability takes 7 fire damage."
ta:
  - name: "Polarize Aura"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** All creatures and objects 
      <br />**Trigger** The dragon is targeted by 2 melee attacks in a single turn.
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 push 5
      <br />★ 12–16 push 7
      <br />✸ 17+ push 10 (ignores stability) "
  - name: "Hammer and Anvil (Free Triggered Action)"
    desc: "
      <br />**Cost** 1 Malice
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** The dragon starts their turn or moves while flying. 
      <br />**Effect:** The dragon plumets to the ground and uses Forge Hammer Tail. They deal an additional 4 damage for each square they fell."
va:
  - name: "Heart of the Forge (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic, Melee
      <br />**Distance** 6 burst
      <br />**Target** All enemies
      <br />`dice: 2d10 + 4`
      <br />✦ ≤11 4 fire damage; I< 2 [[frightened]] (save ends)
      <br />★ 12–16 6 fire damage; I< 3 [[frightened]] (save ends)
      <br />✸ 17+ 8 fire damage; I< 4 [[frightened]] (save ends) 
      <br />**Effect:** The dragon roars, venting scorching air in every direction."
  - name: "Subdermal Shielding (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Effect:** Shields embedded under their scales emerge, giving the dragon damage immunity 6 at the start of each round for the rest of the encounter. The dragon loses this immunity for the rest of the round if they take any damage."
  - name: "Polarity Chaos (Villain Action 3)"
    desc: "
      <br />**Keywords** Area, Magic, Melee, Ranged
      <br />**Distance** 10 burst
      <br />**Target** All creatures and objects in the burst 
      <br />**Effect:** The dragon charges their wyrmscale aura, whipping metal into a magnetized frenzy. Each target makes an Might test.
      <br />`dice: 2d10 + 4`
      <br />✸ ≤11 16 damage; M< 4 pull 10 or push 10
      <br />★ 12–16 13 damage; M< 3 pull 8 or push 8
      <br />✦ 17+ 7 damage, M< 2 pull 5 or push 5"

```

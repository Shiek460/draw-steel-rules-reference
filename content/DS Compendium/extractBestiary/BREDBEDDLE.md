# BREDBEDDLE
```statblock
name: "BREDBEDDLE"
level: 3
roles:
  - SOLO
ancestry:
  - Bredbeddle
  - Giant
ev: 50
stamina: 300
speed: 5
size: 2 /
stability: 4
free_strike: 6
characteristics:
  - +3
  - 0
  - −3
  - +1
  - +2
traits:
  - name: "Solo Monster"
    desc: "- **Solo Turns** The bredbeddle takes up to two turns each round. They can’t take turns consecutively. They can use two actions on each of their turns. While [[dazed]], the bredbeddle can take one action and one maneuver per turn."
  - name: "End Effect"
    desc: "At the end of their turn, the bredbeddle can take 5 damage to end one save ends effect affecting them. This damage can’t be reduced in any way."
  - name: "Resilient Form"
    desc: "The bredbeddle can’t be physically transformed in any way except by their Heady or Not trait."
  - name: "Heady or Not"
    desc: "While headless, the bredbeddle can move into a space with a severed head and attach it to their neck as an action. Doing so physically transforms the bredbeddle, who takes on the size, weight, reach, and stability of the head’s original owner. These effects last until the bredbeddle is killed or beheaded, or until the head falls off after 24 hours. A head that falls off this way can no longer be attached to the bredbeddle. A creature must succeed on a hard Might test made as a maneuver to rip a head off the bredbeddle. If they fail, the bredbeddle makes a free strike against them."
actions:
  - name: "Executioner’s Swing"
    desc:
      "
      <br />**Type:** Signature
      <br />**Keywords** Area, Melee, Weapon
      <br />**Distance** 2 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 2 damage; A<  1 [[bleeding]] (save ends)
      <br />★ 12–16 4 damage; A<  2 [[bleeding]] (save ends)
      <br />✸ 17+ 5 damage; A<  3 [[bleeding]] (save ends); M<  2 [[dazed]] (save ends) 
      <br />**3 Malice** The bredbeddle shifts up to 2 squares and can target additional enemies who come within distance of this ability during the move."
  - name: "Lop"
    desc:
      "
      <br />**Keywords** Magic, Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** One creature
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; [[bleeding]] (save ends) or M<  1 beheaded (see effect)
      <br />★ 12–16 13 damage; [[bleeding]] (save ends) or M<  2 beheaded (see effect)
      <br />✸ 17+ 16 damage; [[bleeding]] (save ends) or M<  3 beheaded (see effect) 
      <br />**Effect:** A beheaded target has their head fall into an unoccupied square adjacent to the bredbeddle, but they remain alive. While beheaded, the target is [[bleeding]] and can’t establish [[Line of Effect]] beyond 1 square. The beheaded target can survive without their head for 24 hours, and can reattach their head with a maneuver by entering its square. A target who remains beheaded for 24 hours dies."
maneuvers:
  - name: "Scramble"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Self (while headless)
      <br />**Target** Self 
      <br />**Effect:** The bredbeddle shifts up to their speed, and can push each creature who comes within their reach during the movement 1 square. Each square the bredbeddle exits during the movement becomes difficult terrain."
  - name: "Headway"
    desc: "
      <br />**Keywords** Ranged, Strike, Weapon
      <br />**Distance** Ranged 20
      <br />**Target** One creature or object 
      <br />**Effect:** The bredbeddle must have a head in their possession (attached to them or not), which they throw at the target. If the head was attached, the bredbeddle becomes headless.
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 9 damage; M<  1 [[dazed]] (save ends)
      <br />★ 12–16 13 damage; [[prone]]; M<  2 [[dazed]] (save ends)
      <br />✸ 17+ 16 damage; [[prone]]; M<  3 [[dazed]] (save ends)"
ta:
  - name: "Envious Imitation"
    desc: "<br />**Cost** 2 Malice
      <br />**Keywords** Magic
      <br />**Distance** Self
      <br />**Target** Self 
      <br />**Trigger** A creature targets the bredbeddle with a ranged strike. 
      <br />**Effect:** The bredbeddle uses the same ability against the triggering creature, using that creature’s bonus to any power rolls they have to make."
va:
  - name: "Turn Green (Villain Action 1)"
    desc: "
      <br />**Keywords** Area, Magic
      <br />**Distance** 3 burst
      <br />**Target** Each enemy in the burst
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 P<  1 The target turns green (save ends)
      <br />★ 12–16 P<  2 The target turns green (save ends)
      <br />✸ 17+ P<  3 The target turns green until the end of the encounter 
      <br />**Effect:** Green shadows crawl out from under the bredbeddle’s feet and attempt to turn each target green. The bredbeddle has a double edge on attacks made against targets turned green until the condition ends."
  - name: "Challenge (Villain Action 2)"
    desc: "
      <br />**Keywords** —
      <br />**Distance** Ranged 5
      <br />**Target** One enemy 
      <br />**Effect:** The bredbeddle points at the target and issues them a challenge. If the target refuses, they turn green until the end of the encounter (see Turn Green). If the target accepts, the bredbeddle shifts to a space adjacent to the target, who must make a hard Might test with no additional modifiers. On success, the target can choose to deal 40 damage to the bredbeddle or remove the bredbeddle’s head. On failure, the target is beheaded (see Lop)."
  - name: "Headlam Rampage (Villain Action 3)"
    desc: "
      <br />**Keywords** Melee, Strike, Weapon
      <br />**Distance** Melee 2
      <br />**Target** Four creatures
      <br />`dice: 2d10 + 3`
      <br />✦ ≤11 6 damage; [[bleeding]] (save ends) or A<  1 beheaded
      <br />★ 12–16 7 damage; [[bleeding]] (save ends) or A<  2 beheaded
      <br />✸ 17+ 8 damage; [[bleeding]] (save ends) or A<  3 beheaded (see Lop)"

```

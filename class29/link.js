class Link{
    constructor(bodyA,bodyB){
        var lastLink= bodyA.body.bodies.length-2;
        this.link= Constraint.create(
            {
            bodyA: bodyA.body.bodies[lastLink],
            PointA:{x:0,y:0},
            bodyB: bodyB,
            PointB:{x:0,y:0},
            length: -10,
            stiffness: 0.01

            });
        World.add(engine.world,this.link);
    }
}
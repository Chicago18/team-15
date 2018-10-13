class mainGame extends Phaser.Scene {
    constructor()
    {
        super({key:"mainGame"});
    }

    preload()
    {

        this.load.image('asteroidNoun', 'Assets/asteroidNoun.png');
        this.load.image('asteroidVerb', 'Assets/asteroidVerb.png');
        this.load.image('asteroidAdj', 'Assets/asteroidAdj.png');
        this.load.image('enemy', 'Assets/bullet.png');
        this.load.image('bullet', 'Assets/bullet.png');
        this.load.audio('pew', 'Assets/pew.mp3');
        this.load.audio('ow', 'Assets/ow.mp3');
        this.load.audio('explosion', 'Assets/explosion.mp3');
        this.load.image('ship', 'Assets/ship.png');
        this.load.image('background', 'Assets/background.jpg');
    }

    create()
    {
        this.add.image(1000,400,'background');
        this.add.image(0,400,'background');
        this.add.image(3000,400,'background');
        this.add.image(1000,800,'background');
        this.add.image(0,800,'background');
        this.add.image(3000,800,'background');
        score = 0;
        scoreText = this.add.text(16, 16, 'score: 0', { fontSize: '48px'});
        var warning = this.add.text(800, 16, 'This game does not work in chrome', { fontSize: '24px'});
        spawnTimer = this.time.addEvent({ delay: 150, callback: spawnAsteroid, callbackScope: this, repeat: 1});
        var scene = this;
        player = this.physics.add.sprite(700,400,'ship');
        enemies = this.physics.add.group();
        /*enemies.children.iterate(function (child) {

          child.setVelocityX(Phaser.Math.RND.integerInRange(-20,-500));
          child.setDisplaySize(80, 80);

        });*/
        gunType = "noun";
        gunText = this.add.text(675, 0, gunType, { fontSize: '48px'});
        var bullets = this.physics.add.group();
        this.key_W = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.W);
        this.key_A = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.A);
        this.key_S = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.S);
        this.key_D = this.input.keyboard.addKey(Phaser.Input.Keyboard.KeyCodes.D);

        this.sound.add("pew");

        this.input.on('pointerdown', function(event)
        {
          var bullet = bullets.create(player.x, player.y, "bullet");
          var xVel = (event.x-player.x);
          var yVel = (event.y-player.y);
          var speed = Math.sqrt(Math.pow(xVel,2) + Math.pow(yVel,2));
          bullet.setVelocity(500*(xVel/speed),500*(yVel/speed));
          bullet.setDisplaySize(10, 10);
          this.sound.play('pew');
        }, this);

        this.input.keyboard.on('keyup_ONE', function (e)
        {
                changeGun("noun");
        }, this);

        this.input.keyboard.on('keyup_TWO', function (e)
        {
                changeGun("verb");
        }, this);

        this.input.keyboard.on('keyup_THREE', function (e)
        {
                changeGun("adj");
        }, this);

        this.physics.add.overlap(bullets, enemies, enemyHit, null, this);
        this.physics.add.collider(enemies, enemies);

        this.physics.add.overlap(player, enemies, playerHit, null, this);

    }

    update(delta)
    {
        if(this.key_A.isDown)
        {
            player.x = player.x - 2;
        }
        if(this.key_W.isDown)
        {
            player.y = player.y - 2;
        }
        if(this.key_S.isDown)
        {
            player.y = player.y + 2;
        }
        if(this.key_D.isDown)
        {
            player.x = player.x + 2;
        }
    }
}

var config = {
    type:Phaser.AUTO,
    width:4000,
    height:800,
    physics: {
        default:'arcade',
        arcade: {
        }
    },
    scene: [mainGame]
};
var score;
var scoreText;
var game = new Phaser.Game(config);
var player;
var enemies;
var spawnTimer;
var gunType;
var gunText;
var enemyText;
function enemyHit (bullet, enemies)
{
    if(enemies.name == gunType)
    {
        enemies.disableBody(true, true);
        this.sound.play('explosion');
        score += 10;
        scoreText.setText('Score: ' + score);
    }
    bullet.disableBody(true,true);
}
function playerHit (player, enemies)
{
    enemies.disableBody(true, true);
    this.sound.play('ow');
    this.physics.pause();
    player.setTint(0xff0000);
}

function spawnAsteroid()
{
    rand = Phaser.Math.RND.integerInRange(1,4);
    if(rand == 1)
    {
        x = Phaser.Math.RND.integerInRange(-200,1700);
        y = -50;
        yVel = Phaser.Math.RND.integerInRange(20,500);
        xVel = Phaser.Math.RND.integerInRange(-500,500);
    }
    else if(rand == 2)
    {
        x = Phaser.Math.RND.integerInRange(-200,1700);
        y = 850;
        yVel = Phaser.Math.RND.integerInRange(-500,-20);
        xVel = Phaser.Math.RND.integerInRange(-500,500);
    }
    else if(rand == 3)
    {
        x = -50;
        y = Phaser.Math.RND.integerInRange(-100,900);
        yVel = Phaser.Math.RND.integerInRange(-300,300);
        xVel = Phaser.Math.RND.integerInRange(20,500);
    }
    else
    {
        x = -50;
        y = Phaser.Math.RND.integerInRange(-100,900);
        yVel = Phaser.Math.RND.integerInRange(-300,300);
        xVel = Phaser.Math.RND.integerInRange(-500,-20);
    }

    var astType = Phaser.Math.RND.integerInRange(1,4);

    if(astType == 1)
    {
      ast = enemies.create(x, y, 'asteroidNoun');
      ast.name = "noun";
    }
    else if(astType == 2)
    {
      ast = enemies.create(x, y, 'asteroidVerb');
      ast.name = "verb";
    }
    else
    {
      ast = enemies.create(x, y, 'asteroidAdj');
      ast.name = "adj";
    }
    ast.setVelocity(xVel,yVel);
    ast.setDisplaySize(80, 80);
    spawnTimer.reset({delay: 300, callback: spawnAsteroid, callbackScope: this, repeat: 1});
}

function changeGun(type)
{
    gunType = type;
    gunText.setText(type);
}

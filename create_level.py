import pygame
import Block
import KillBlock


def create_lvl(height, block_sprites, kill_sprites):
    for _ in range(height-192, height, 128):
        for i in range(9):
            block_sprites.add(Block.Block(64+128*i, _))
        for i in range(13):
            block_sprites.add(Block.Block(1728+128*i, _)) #1
    for i in range(9):
        block_sprites.add(Block.Block(64 + 128 * i, height+64))
    for i in range(7):
        block_sprites.add(Block.Block(1664-64 + 128 * i, height+64))
    for i in range(2):
        block_sprites.add(Block.Block(3200 - 64 + 128 * i, height + 64)) #3
    for i in range(9):
        block_sprites.add(Block.Block(64 + 128 * i, height+192))
    for i in range(4):
        block_sprites.add(Block.Block(128*15-64+128 * i, height+192))
    block_sprites.add(Block.Block(3200+64, height+192)) #4
    for i in range(2):
        block_sprites.add(Block.Block(64 + 128 * i, height+320))
    for i in range(3):
        block_sprites.add(Block.Block(128*8-64 + 128 * i, height+320))
    for i in range(3):
        block_sprites.add(Block.Block(128*15-64 + 128 * i, height+320)) #5
    block_sprites.add(Block.Block(64, height + 320+128))
    for i in range(3):
        block_sprites.add(Block.Block(128*15-64 + 128 * i, height+320+128)) #6
    block_sprites.add(Block.Block(64, height + 320+128*2))
    for i in range(4):
        block_sprites.add(Block.Block(128*14-64 + 128 * i, height+320+128*2))
    for i in range(5):
        block_sprites.add(Block.Block(128*21-64 + 128 * i, height+320+128*2)) #7
    block_sprites.add(Block.Block(64, height + 320 + 128 * 3))
    for i in range(5):
        block_sprites.add(Block.Block(128*13-64 + 128 * i, height+320+128*3))
    for i in range(7):
        block_sprites.add(Block.Block(128 * 20 - 64 + 128 * i, height + 320 + 128 * 3)) #8
    block_sprites.add(Block.Block(64, height + 320 + 128 * 4))
    for i in range(4):
        block_sprites.add(Block.Block(128 * 10 - 64 + 128 * i, height + 320 + 128 * 4))
    for i in range(3):
        block_sprites.add(Block.Block(128 * 15 - 64 + 128 * i, height + 320 + 128 * 4))
    for i in range(7):
        block_sprites.add(Block.Block(128 * 20 - 64 + 128 * i, height + 320 + 128 * 4))
    for i in range(10):
        kill_sprites.add(KillBlock.Block(128 * 27 - 64 + 128 * i, height + 320 + 128 * 4)) #9
    block_sprites.add(Block.Block(64, height + 320 + 128 * 5))
    block_sprites.add(Block.Block(128*16-64, height + 320 + 128 * 5))
    block_sprites.add(Block.Block(128 * 20 - 64,  height + 320 + 128 * 5)) #10
    for i in range(7):
        block_sprites.add(Block.Block(64 + 128*i, height + 320 + 128 * 6))
    block_sprites.add(Block.Block(128 * 19 - 64, height + 320 + 128 * 6)) #11
    for i in range(8):
        block_sprites.add(Block.Block(64+128*i, height + 320 + 128 * 7)) #12
    for i in range(4):
        block_sprites.add(Block.Block(128*5-64+128*i, height + 320 + 128 * 8)) #13
    for i in range(4):
        block_sprites.add(Block.Block(128*7-64+128*i, height + 320 + 128 * 9))
    for i in range(11):
        block_sprites.add(Block.Block(128*24-64+128*i, height + 320 + 128 * 9)) # 0
    for i in range(8):
        block_sprites.add(Block.Block(128*8-64+128*i, height + 320 + 128 * 10))
    for i in range(12):
        block_sprites.add(Block.Block(128*23-64+128*i, height + 320 + 128 * 10)) #-1
    for i in range(9):
        block_sprites.add(Block.Block(128*10-64+128*i, height + 320 + 128 * 11))
    for i in range(13):
        block_sprites.add(Block.Block(128*22-64+128*i, height + 320 + 128 * 11)) #-2
    block_sprites.add(Block.Block(128 * 11 - 64, height + 320 + 128 * 12))
    for i in range(6):
        block_sprites.add(Block.Block(128*13-64+128*i, height + 320 + 128 * 12))
    for i in range(14):
        block_sprites.add(Block.Block(128*21-64+128*i, height + 320 + 128 * 12))  #-3
    for i in range(3):
        block_sprites.add(Block.Block(64+128*i, height + 320 + 128 * 13))
    for i in range(4):
        block_sprites.add(Block.Block(128*14-64+128*i, height + 320 + 128 * 13))
    for i in range(12):
        block_sprites.add(Block.Block(128*23-64+128*i, height + 320 + 128 * 13)) #-4
    for i in range(2):
        block_sprites.add(Block.Block(128*3-64+128*i, height + 320 + 128 * 14))
    for i in range(4):
        block_sprites.add(Block.Block(128*15-64+128*i, height + 320 + 128 * 14))
    for i in range(10):
        block_sprites.add(Block.Block(128*25-64+128*i, height + 320 + 128 * 14)) #-5
    for i in range(2):
        block_sprites.add(Block.Block(128*6-64+128*i, height + 320 + 128 * 15))
    block_sprites.add(Block.Block(128 * 16 - 64, height + 320 + 128 * 15))
    for i in range(2):
        block_sprites.add(Block.Block(128*19-64+128*i, height + 320 + 128 * 15))
    for i in range(10):
        block_sprites.add(Block.Block(128*25-64+128*i, height + 320 + 128 * 15)) #-6
    block_sprites.add(Block.Block(128 * 10 - 64, height + 320 + 128 * 16))
    for i in range(10):
        block_sprites.add(Block.Block(128*25-64+128*i, height + 320 + 128 * 16)) #-7
    for i in range(2):
        block_sprites.add(Block.Block(128*12-64+128*i, height + 320 + 128 * 17))
    for i in range(11):
        block_sprites.add(Block.Block(128*24-64+128*i, height + 320 + 128 * 17)) #-8
    for i in range(12):
        block_sprites.add(Block.Block(128*23-64+128*i, height + 320 + 128 * 18)) #-9
    for i in range(20):
        block_sprites.add(Block.Block(128*15-64+128*i, height + 320 + 128 * 19)) #-10
    for i in range(18):
        block_sprites.add(Block.Block(128*17-64+128*i, height + 320 + 128 * 20)) #-11
    for i in range(16):
        kill_sprites.add(KillBlock.Block(64+128*i, height + 320 + 128 * 20))
    for i in range(17):
        block_sprites.add(Block.Block(128*18-64+128*i, height + 320 + 128 * 21)) #-12
    for i in range(34):
        block_sprites.add(Block.Block(64+128*i, height + 320 + 128 * 22)) #-13

    return block_sprites, kill_sprites

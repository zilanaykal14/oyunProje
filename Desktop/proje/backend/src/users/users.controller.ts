import { Controller, Get, Post, Body, Param } from '@nestjs/common';
import { UsersService } from './users.service';
import { CreateUserDto } from './dto/create-user.dto';

@Controller('users')
export class UsersController {
  constructor(private readonly usersService: UsersService) {}

  // POST localhost:3000/users -> Yeni kullanıcı kaydeder
  @Post()
  create(@Body() createUserDto: CreateUserDto) {
    return this.usersService.create(createUserDto);
  }

  // GET localhost:3000/users -> Tüm kullanıcıları getirir
  @Get()
  findAll() {
    return this.usersService.findAll();
  }

  // GET localhost:3000/users/5 -> ID'si 5 olan kullanıcıyı getirir
  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.usersService.findOne(+id);
  }
}

import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { CreateUserDto } from './dto/create-user.dto';
import { User } from './entities/user.entity';
import * as bcrypt from 'bcrypt';

@Injectable()
export class UsersService {
  constructor(
    @InjectRepository(User)
    private userRepository: Repository<User>,
  ) {}

  // YENİ HALİ: Şifreyi hashleyip kaydeder
  async create(createUserDto: CreateUserDto) {
    const salt = await bcrypt.genSalt(); // Rastgele tuz oluştur
    const hashedPassword = await bcrypt.hash(createUserDto.password, salt); // Şifreyi karıştır

    const newUser = this.userRepository.create({
      ...createUserDto,
      password: hashedPassword, // Veritabanına karışık halini yaz
    });
    return await this.userRepository.save(newUser);
  }

  findAll() {
    return this.userRepository.find();
  }

  findOne(id: number) {
    return this.userRepository.findOneBy({ id });
  }

  findByEmail(email: string) {
    return this.userRepository.findOneBy({ email });
  }
}

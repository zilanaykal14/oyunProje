import { Injectable, UnauthorizedException } from '@nestjs/common';
import { UsersService } from '../users/users.service';
import { JwtService } from '@nestjs/jwt';
import * as bcrypt from 'bcrypt';
import { LoginDto } from './dto/login.dto';

@Injectable()
export class AuthService {
  constructor(
    private usersService: UsersService,
    private jwtService: JwtService,
  ) {}

  async login(loginDto: LoginDto) {
    // 1. Kullanıcıyı email ile bul
    const user = await this.usersService.findByEmail(loginDto.email);
    if (!user) {
      throw new UnauthorizedException('Kullanıcı bulunamadı.');
    }

    // 2. Şifreyi kontrol et (Hashlenmiş şifre ile karşılaştır)
    const isPasswordMatching = await bcrypt.compare(
      loginDto.password,
      user.password,
    );

    if (!isPasswordMatching) {
      throw new UnauthorizedException('Şifre hatalı.');
    }

    // 3. Her şey doğruysa Token oluştur
    const payload = {
      sub: user.id,
      email: user.email,
      role: user.role,
      firstName: user.firstName, // <-- YENİ EKLENDİ
      lastName: user.lastName, // <-- YENİ EKLENDİ
    };

    return {
      access_token: await this.jwtService.signAsync(payload),
      user: {
        id: user.id,
        firstName: user.firstName,
        role: user.role,
      },
    };
  }
}

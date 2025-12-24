import { Module } from '@nestjs/common';
import { TypeOrmModule } from '@nestjs/typeorm';
import { ConfigModule, ConfigService } from '@nestjs/config';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { UsersModule } from './users/users.module';
import { StudentsModule } from './students/students.module';
import { CoursesModule } from './courses/courses.module';
import { EnrollmentsModule } from './enrollments/enrollments.module';
import { AuthModule } from './auth/auth.module';

@Module({
  imports: [
    ConfigModule.forRoot({ isGlobal: true }),

    // VERİTABANI BAĞLANTISI (POSTGRESQL)
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      useFactory: (configService: ConfigService) => ({
        type: 'postgres', // <-- ARTIK POSTGRES
        url: configService.get('DATABASE_URL'), // <-- Linki .env'den alıyor
        autoLoadEntities: true,
        synchronize: true, // Tabloları otomatik oluşturur
        ssl: {
          rejectUnauthorized: false, // Bulut bağlantısı için gerekli izin
        },
      }),
      inject: [ConfigService],
    }),

    UsersModule,
    StudentsModule,
    CoursesModule,
    EnrollmentsModule,
    AuthModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

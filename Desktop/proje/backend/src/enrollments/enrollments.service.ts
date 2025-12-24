import { ConflictException, Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { CreateEnrollmentDto } from './dto/create-enrollment.dto';
import { Enrollment } from './entities/enrollment.entity';

@Injectable()
export class EnrollmentsService {
  constructor(
    @InjectRepository(Enrollment)
    private enrollmentRepository: Repository<Enrollment>,
  ) {}

  async create(createEnrollmentDto: CreateEnrollmentDto) {
    // 1. Kontrol: Bu öğrenci bu kursa zaten kayıtlı mı?
    const existingEnrollment = await this.enrollmentRepository.findOne({
      where: {
        student: { id: createEnrollmentDto.studentId },
        course: { id: createEnrollmentDto.courseId },
      },
    });

    // 2. Eğer kayıt varsa hata fırlat (409 Conflict Hatası)
    if (existingEnrollment) {
      throw new ConflictException('Bu öğrenci bu kursa zaten kayıtlı!');
    }

    // 3. Kayıt yoksa yeni kaydı oluştur
    const newEnrollment = this.enrollmentRepository.create({
      student: { id: createEnrollmentDto.studentId },
      course: { id: createEnrollmentDto.courseId },
      enrollmentDate: new Date(),
    });

    return this.enrollmentRepository.save(newEnrollment);
  }

  findAll() {
    // Kayıtları getirirken hem öğrenciyi hem kursu göster
    return this.enrollmentRepository.find({
      relations: ['student', 'course'],
    });
  }
}

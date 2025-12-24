import { Injectable } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { CreateStudentDto } from './dto/create-student.dto';
import { Student } from './entities/student.entity';
import { UpdateStudentDto } from './dto/update-student.dto';

@Injectable()
export class StudentsService {
  constructor(
    @InjectRepository(Student)
    private studentRepository: Repository<Student>,
  ) {}

  async create(createStudentDto: CreateStudentDto) {
    // DTO'dan gelen parentId'yi kullanarak ilişkiyi kuruyoruz
    const newStudent = this.studentRepository.create({
      ...createStudentDto,
      parent: { id: createStudentDto.parentId }, // İlişki burada kuruluyor
    });
    return await this.studentRepository.save(newStudent);
  }
  // GÜNCELLEME İŞLEMİ
  async update(id: number, updateStudentDto: UpdateStudentDto) {
    // Önce öğrenci var mı kontrol et
    const student = await this.studentRepository.findOne({ where: { id } });
    if (!student) {
      throw new Error('Öğrenci bulunamadı');
    }

    // Güncelle ve kaydet
    await this.studentRepository.update(id, updateStudentDto);
    return this.findOne(id);
  }

  // SİLME İŞLEMİ (KESİN ÇÖZÜM)
  async remove(id: number) {
    // 1. Öğrenciyi, ilişkili kayıtlarıyla (enrollments) birlikte bul
    const student = await this.studentRepository.findOne({
      where: { id },
      relations: ['enrollments'],
    });

    // 2. Eğer öğrenci varsa, TypeORM'un 'remove' metoduyla sil
    // (remove metodu, entity dosyasındaki 'cascade' ayarını çalıştırır)
    if (student) {
      return this.studentRepository.remove(student);
    }
    return { deleted: true };
  }

  findAll() {
    // İlişkili olduğu veliyi (parent) de getirir
    return this.studentRepository.find({
      relations: ['parent', 'enrollments', 'enrollments.course'],
    });
  }

  findOne(id: number) {
    return this.studentRepository.findOne({
      where: { id },
      relations: ['parent', 'enrollments'],
    });
  }
}

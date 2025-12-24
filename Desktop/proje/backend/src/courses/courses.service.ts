import { Injectable, NotFoundException } from '@nestjs/common';
import { InjectRepository } from '@nestjs/typeorm';
import { Repository } from 'typeorm';
import { CreateCourseDto } from './dto/create-course.dto';
import { Course } from './entities/course.entity';
import { UpdateCourseDto } from './dto/update-course.dto';

@Injectable()
export class CoursesService {
  constructor(
    @InjectRepository(Course)
    private courseRepository: Repository<Course>,
  ) {}

  async create(createCourseDto: CreateCourseDto) {
    const newCourse = this.courseRepository.create({
      ...createCourseDto,
      teacher: { id: createCourseDto.teacherId },
    });
    return await this.courseRepository.save(newCourse);
  }

  findAll() {
    // relations içinde 'enrollments' olduğuna DİKKAT (yazım hatası olmasın)
    return this.courseRepository.find({
      relations: ['teacher', 'enrollments', 'enrollments.student'],
    });
  }

  findOne(id: number) {
    return this.courseRepository.findOne({
      where: { id },
      relations: ['teacher', 'enrollments'],
    });
  }

  // --- YENİ EKLENEN: GÜNCELLEME ---
  async update(id: number, updateCourseDto: UpdateCourseDto) {
    // Update işlemi time verisini de kapsayacak şekilde yapılır
    await this.courseRepository.update(id, updateCourseDto);
    return this.findOne(id); // Güncel halini geri dön
  }

  // --- YENİ EKLENEN: SİLME ---
  async remove(id: number) {
    const course = await this.findOne(id);
    if (!course) {
      throw new NotFoundException('Kurs bulunamadı');
    }
    return this.courseRepository.remove(course);
  }
}

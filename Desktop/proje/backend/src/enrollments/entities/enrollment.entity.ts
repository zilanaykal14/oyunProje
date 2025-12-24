import { Entity, PrimaryGeneratedColumn, CreateDateColumn, Column, ManyToOne } from 'typeorm';
import { Student } from '../../students/entities/student.entity';
import { Course } from '../../courses/entities/course.entity';

@Entity('enrollments')
export class Enrollment {
  @PrimaryGeneratedColumn()
  id: number;

  @CreateDateColumn()
  enrollmentDate: Date;

  @Column({ default: 'ACTIVE' })
  status: string; // ACTIVE, COMPLETED, CANCELLED

  // İLİŞKİ: Hangi Öğrenci?
  @ManyToOne(() => Student, (student) => student.enrollments, { onDelete: 'CASCADE' })
  student: Student;

  // İLİŞKİ: Hangi Kurs?
  @ManyToOne(() => Course, (course) => course.enrollments, { onDelete: 'CASCADE' })
  course: Course;
}

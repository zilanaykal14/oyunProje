import {
  Entity,
  PrimaryGeneratedColumn,
  Column,
  CreateDateColumn,
  OneToMany,
} from 'typeorm';
import { Student } from '../../students/entities/student.entity';
import { Course } from '../../courses/entities/course.entity';

export enum UserRole {
  TEACHER = 'TEACHER', // Öğretmen
  PARENT = 'PARENT', // Veli
}

@Entity('users')
export class User {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  firstName: string;

  @Column()
  lastName: string;

  @Column({ unique: true })
  email: string;

  @Column()
  password: string; // Gerçek projede hashlenmiş olmalı

  @Column({
    type: 'enum',
    enum: UserRole,
    default: UserRole.PARENT,
  })
  role: UserRole;

  @CreateDateColumn()
  createdAt: Date;

  // İLİŞKİLER (Daha sonra diğer tabloları yazınca buradaki kırmızı hatalar gidecek)

  // Bir Veli'nin birden fazla öğrencisi olabilir
  @OneToMany(() => Student, (student) => student.parent)
  students: Student[];

  // Bir Öğretmen'in birden fazla kursu olabilir
  @OneToMany(() => Course, (course) => course.teacher)
  courses: Course[];
}

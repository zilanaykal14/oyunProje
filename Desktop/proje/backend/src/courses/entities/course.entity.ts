import {
  Entity,
  PrimaryGeneratedColumn,
  Column,
  ManyToOne,
  OneToMany,
} from 'typeorm';
import { User } from '../../users/entities/user.entity';
import { Enrollment } from '../../enrollments/entities/enrollment.entity';

@Entity('courses')
export class Course {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  title: string;

  @Column('text')
  description: string;

  @Column()
  quota: number; // Kontenjan

  @Column({ nullable: true }) // nullable: true dedik ki eski kurslar hata vermesin
  time: string;

  // İLİŞKİ: Bu kursu veren bir öğretmen vardır (User tablosuna bağlanır)
  @ManyToOne(() => User, (user) => user.courses, { onDelete: 'CASCADE' })
  teacher: User;

  // İLİŞKİ: Bu kursa yapılmış kayıtlar
  @OneToMany(() => Enrollment, (enrollment) => enrollment.course)
  enrollments: Enrollment[];
}

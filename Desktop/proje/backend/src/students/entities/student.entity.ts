import {
  Entity,
  PrimaryGeneratedColumn,
  Column,
  ManyToOne,
  OneToMany,
} from 'typeorm';
import { User } from '../../users/entities/user.entity';
import { Enrollment } from '../../enrollments/entities/enrollment.entity';

@Entity('students')
export class Student {
  @PrimaryGeneratedColumn()
  id: number;

  @Column()
  fullName: string;

  @Column()
  age: number;

  @Column()
  instrumentInterest: string; // Örn: Piyano, Gitar

  // İLİŞKİ: Bir öğrencinin bir velisi olur (User tablosuna bağlanır)
  @ManyToOne(() => User, (user) => user.students, { onDelete: 'CASCADE' })
  parent: User;

  // İLİŞKİ: Bir öğrencinin birden fazla kurs kaydı olabilir
  @OneToMany(() => Enrollment, (enrollment) => enrollment.student, {
    cascade: true,
    onDelete: 'CASCADE', // ✨ SİHİRLİ KOD: Öğrenci silinirse kayıtları da sil!
  })
  enrollments: Enrollment[];
}

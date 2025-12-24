import { IsNumber, IsString } from 'class-validator';

export class CreateStudentDto {
  @IsString()
  fullName: string;

  @IsNumber()
  age: number;

  @IsString()
  instrumentInterest: string;

  @IsNumber()
  parentId: number;
}

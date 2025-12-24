import { IsNumber, IsString, IsOptional } from 'class-validator';

export class CreateCourseDto {
  @IsString()
  title: string;

  @IsString()
  description: string;

  @IsNumber()
  quota: number;

  @IsString()
  @IsOptional()
  time: string;

  @IsNumber()
  teacherId: number;
}

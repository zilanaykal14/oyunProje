import { Controller, Get, Post, Body } from '@nestjs/common';
import { EnrollmentsService } from './enrollments.service';
import { CreateEnrollmentDto } from './dto/create-enrollment.dto';

@Controller('enrollments')
export class EnrollmentsController {
  constructor(private readonly enrollmentsService: EnrollmentsService) {}

  // POST localhost:3000/enrollments -> Bir öğrenciyi kursa kaydeder
  @Post()
  create(@Body() createEnrollmentDto: CreateEnrollmentDto) {
    return this.enrollmentsService.create(createEnrollmentDto);
  }

  // GET localhost:3000/enrollments -> Kim hangi kursta listeler
  @Get()
  findAll() {
    return this.enrollmentsService.findAll();
  }
}

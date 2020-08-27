import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FavouriteProgramFormComponent } from './favourite-program-form.component';

describe('FavouriteProgramFormComponent', () => {
  let component: FavouriteProgramFormComponent;
  let fixture: ComponentFixture<FavouriteProgramFormComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FavouriteProgramFormComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FavouriteProgramFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

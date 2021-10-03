from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class customer(Base):
    __tablename__ = 'customer'        
    id = Column(Integer, primary_key=True)
    firstName = Column(String)
    lastName = Column(String)
    email = Column(String)
    phone = Column(String)
        
    def __init__(self, firstName, lastName, email, phone):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.phone = phone
        
    def __repr__(self):
        return"<Customer(firstName='%s', lastName='%s', email='%s', phone='%s')>" % (
                                self.firstName, self.lastName, self.email, self.phone)
        
def main():
    engine = create_engine('sqlite:///:memory:',echo=True)
    
    Base.metadata.create_all(engine)
    
    customer1 = customer("Joe", "Smith", "j.smith@gmail.com", "555-1234")
    print(customer1)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    session.add(customer)
    
    newCustomer1 = session.query(Customer).filter_by(firstName).first()
    print(newCustomer1)
    
    print(customer1.id)
    
    session.add_all([
        Customer(firstName='Steve', lastName='Jobs', email='s.j@gmail.com', phone='555-2233'),
        Customer(firstName='Andy', lastName='Kelly', email='a.k@gmail.com',phone='555-3344')])
    session.commit()
    
    for row in session.query(customer).all():
        print(row.firstName, row.lastName)
        
main()

